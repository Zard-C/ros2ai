# Copyright 2023 Tomoya Fujita <tomoya.fujita825@gmail.com>.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

ROS_OPENAI_API_KEY_ENV_VAR = 'OPENAI_API_KEY'

ROS_OPENAI_DEFAULT_MODEL = 'gpt-4'
ROS_OPENAI_MODEL_NAME_ENV_VAR = 'OPENAI_MODEL_NAME'

ROS_OPENAI_DEFAULT_ENDPOINT = 'https://api.openai.com/v1'
ROS_OPENAI_ENDPOINT_ENV_VAR = 'OPENAI_ENDPOINT'

# The system message helps set the behavior of the assistant.
# For example, you can modify the personality of the assistant or provide specific
# instructions about how it should behave throughout the conversation.
# However note that the system message is optional and the model’s behavior without a system message
# is likely to be similar to using a generic message such as "You are a helpful assistant."
# TODO@fujitatomoya: ROS_DISTRO would be better to assistant setting.
ROLE_SYSTEM_QUERY_DEFAULT = 'You are a ROS 2 helpful assistant.'
ROLE_SYSTEM_EXEC_DEFAULT = 'You are a ROS 2 command line executor, provides executable commands only without any comments.'
