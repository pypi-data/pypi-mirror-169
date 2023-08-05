# coding=utf-8
# Copyright 2020 The TF-Agents Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""End-to-end test for bandit training under sparse feature environments."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
from absl import app
from absl import flags
import numpy as np
import tensorflow as tf  # pylint: disable=g-explicit-tensorflow-version-import

from tf_agents.bandits.agents import neural_epsilon_greedy_agent
from tf_agents.bandits.agents import neural_linucb_agent
from tf_agents.bandits.agents.examples.v2 import trainer
from tf_agents.bandits.environments import stationary_stochastic_structured_py_environment as sspe
from tf_agents.bandits.networks import global_and_arm_feature_network
from tf_agents.bandits.specs import utils as bandit_spec_utils
from tf_agents.environments import tf_py_environment
from tf_agents.policies import utils as policy_utilities

flags.DEFINE_string('root_dir', os.getenv('TEST_UNDECLARED_OUTPUTS_DIR'),
                    'Root directory for writing logs/summaries/checkpoints.')

flags.DEFINE_enum(
    'agent', 'epsGreedy', ['epsGreedy', 'NeuralLinUCB'],
    'Which agent to use. Possible values: `epsGreedy` and `NeuralLinUCB`.'
)

flags.DEFINE_bool('drop_arm_obs', False, 'Whether to wipe the arm observations '
                  'from the trajectories.')

FLAGS = flags.FLAGS

# Environment parameters.

DICTIONARY_SIZE = 100
NUM_GLOBAL_FEATURES = 10
NUM_ARM_FEATURES = 11
NUM_ACTIONS = 7

# Driver parameters.

BATCH_SIZE = 16
TRAINING_LOOPS = 2000
STEPS_PER_LOOP = 2

# Parameters for neural agents (NeuralEpsGreedy and NerualLinUCB).

EPSILON = 0.01
LR = 0.05

# Parameters for NeuralLinUCB. ENCODING_DIM is the output dimension of the
# encoding network. This output will be used by either a linear reward layer and
# epsilon greedy exploration, or by a LinUCB logic, depending on the number of
# training steps executed so far. If the number of steps is less than or equal
# to EPS_PHASE_STEPS, epsilon greedy is used, otherwise LinUCB.

ENCODING_DIM = 9
EPS_PHASE_STEPS = 1000


def main(unused_argv):
  tf.compat.v1.enable_v2_behavior()  # The trainer only runs with V2 enabled.

  feature_dict = np.array([str(i) for i in range(DICTIONARY_SIZE)])
  def _global_context_sampling_fn():
    """Generates one sample of global features.

    It generates a dictionary of size `NUM_GLOBAL_FEATURES`, with the following
    syntax:

    {...,
     'global_feature_4': ['43'],
     ...
    }

    That is, the values are one-element numpy arrays of strings.

    Returns:
      A dictionary with string keys and numpy string array values.
    """
    generated_features = feature_dict[np.random.randint(0, DICTIONARY_SIZE,
                                                        [NUM_GLOBAL_FEATURES])]
    global_features = {
        'global_feature_{}'.format(i): generated_features[[i]]
        for i in range(NUM_GLOBAL_FEATURES)
    }
    return global_features

  def _arm_context_sampling_fn():
    """Generates one sample of arm features.

    It generates a dictionary of size `NUM_ARM_FEATURES`, with the following
    syntax:

    {...,
     'arm_feature_7': ['29'],
     ...
    }

    That is, the values are one-element numpy arrays of strings. Note that the
    output sample is for one arm and one non-batched time step.

    Returns:
      A dictionary with string keys and numpy string array values.
    """
    generated_features = feature_dict[np.random.randint(
        0, DICTIONARY_SIZE, [NUM_ARM_FEATURES])]
    arm_features = {
        'arm_feature_{}'.format(i): generated_features[[i]]
        for i in range(NUM_ARM_FEATURES)
    }
    return arm_features

  def _reward_fn(global_features, arm_features):
    """Outputs a [0, 1] float given a sample.

    The output reward is generated by hashing the concatenation of feature keys
    and values, then adding all up, taking modulo by 1000, and normalizing.

    Args:
      global_features: A dictionary with string keys and 1d string numpy array
        values.
      arm_features: A dictionary with string keys and 1d string numpy array
        values.

    Returns:
      A float value between 0 and 1.
    """
    hashed_global = 0
    for x, y in global_features.items():
      hashed_global += hash(x + y[0])
    hashed_arm = 0
    for x, y in arm_features.items():
      hashed_arm += hash(x + y[0])
    return (hashed_global + hashed_arm) % 1000 / 1000

  env = sspe.StationaryStochasticStructuredPyEnvironment(
      _global_context_sampling_fn,
      _arm_context_sampling_fn,
      NUM_ACTIONS,
      _reward_fn,
      batch_size=BATCH_SIZE)
  environment = tf_py_environment.TFPyEnvironment(env)

  def make_string_feature(name):
    return tf.feature_column.indicator_column(
        tf.feature_column.categorical_column_with_vocabulary_list(
            name, feature_dict))

  global_columns = [
      make_string_feature('global_feature_{}'.format(i))
      for i in range(NUM_GLOBAL_FEATURES)
  ]
  arm_columns = [
      make_string_feature('arm_feature_{}'.format(i))
      for i in range(NUM_ARM_FEATURES)
  ]
  obs_spec = environment.observation_spec()
  if FLAGS.agent == 'epsGredy':
    network = (
        global_and_arm_feature_network.create_feed_forward_common_tower_network(
            obs_spec, (4, 3), (3, 4), (4, 2),
            global_preprocessing_combiner=tf.compat.v2.keras.layers
            .DenseFeatures(global_columns),
            arm_preprocessing_combiner=tf.compat.v2.keras.layers.DenseFeatures(
                arm_columns)))
    agent = neural_epsilon_greedy_agent.NeuralEpsilonGreedyAgent(
        time_step_spec=environment.time_step_spec(),
        action_spec=environment.action_spec(),
        reward_network=network,
        optimizer=tf.compat.v1.train.AdamOptimizer(learning_rate=LR),
        epsilon=EPSILON,
        accepts_per_arm_features=True,
        emit_policy_info=policy_utilities.InfoFields.PREDICTED_REWARDS_MEAN)
  elif FLAGS.agent == 'NeuralLinUCB':
    network = (
        global_and_arm_feature_network.create_feed_forward_common_tower_network(
            obs_spec, (40, 30), (30, 40), (40, 20),
            ENCODING_DIM,
            global_preprocessing_combiner=tf.compat.v2.keras.layers
            .DenseFeatures(global_columns),
            arm_preprocessing_combiner=tf.compat.v2.keras.layers.DenseFeatures(
                arm_columns)))
    agent = neural_linucb_agent.NeuralLinUCBAgent(
        time_step_spec=environment.time_step_spec(),
        action_spec=environment.action_spec(),
        encoding_network=network,
        encoding_network_num_train_steps=EPS_PHASE_STEPS,
        encoding_dim=ENCODING_DIM,
        optimizer=tf.compat.v1.train.AdamOptimizer(learning_rate=LR),
        alpha=1.0,
        gamma=1.0,
        epsilon_greedy=EPSILON,
        accepts_per_arm_features=True,
        debug_summaries=True,
        summarize_grads_and_vars=True,
        emit_policy_info=policy_utilities.InfoFields.PREDICTED_REWARDS_MEAN)

  if FLAGS.drop_arm_obs:
    drop_arm_feature_fn = bandit_spec_utils.drop_arm_observation
  else:
    drop_arm_feature_fn = None
  trainer.train(
      root_dir=FLAGS.root_dir,
      agent=agent,
      environment=environment,
      training_loops=TRAINING_LOOPS,
      steps_per_loop=STEPS_PER_LOOP,
      training_data_spec_transformation_fn=drop_arm_feature_fn)


if __name__ == '__main__':
  app.run(main)
