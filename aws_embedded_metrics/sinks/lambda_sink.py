# Copyright 2019 Amazon.com, Inc. or its affiliates.
# Licensed under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from aws_embedded_metrics.logger.metrics_context import MetricsContext
from aws_embedded_metrics.sinks import Sink
from aws_embedded_metrics.serializers import Serializer
from aws_embedded_metrics.serializers.log_serializer import LogSerializer


class LambdaSink(Sink):
    def __init__(self, serializer: Serializer = LogSerializer()):
        self.serializer = serializer

    def accept(self, context: MetricsContext) -> None:
        print(self.serializer.serialize(context))

    @staticmethod
    def name() -> str:
        return "LambdaSink"
