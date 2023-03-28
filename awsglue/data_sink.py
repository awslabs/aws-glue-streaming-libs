# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from awsglue.dynamicframe import DynamicFrame, DynamicFrameCollection
from awsglue.utils import makeOptions, callsite
from pyspark.sql import DataFrame

class DataSink(object):
    def __init__(self, j_sink, sql_ctx):
        self._jsink = j_sink
        self._sql_ctx = sql_ctx

    def setFormat(self, format, **options):
        self._jsink.setFormat(format, makeOptions(self._sql_ctx._sc, options))

    def setAccumulableSize(self, size):
        self._jsink.setAccumulableSize(size)

    def setCatalogInfo(self, catalogDatabase, catalogTableName, catalogId = ""):
        self._jsink.setCatalogInfo(catalogDatabase, catalogTableName, catalogId)

    def writeFrame(self, dynamic_frame, info = ""):
        return DynamicFrame(self._jsink.pyWriteDynamicFrame(dynamic_frame._jdf, callsite(), info), dynamic_frame.glue_ctx, dynamic_frame.name + "_errors")

    def writeDataFrame(self, data_frame, glue_context, info = ""):
        return DataFrame(self._jsink.pyWriteDataFrame(data_frame._jdf, glue_context._glue_scala_context, callsite(), info), self._sql_ctx)

    def write(self, dynamic_frame_or_dfc, info = ""):
        if isinstance(dynamic_frame_or_dfc, DynamicFrame):
            return self.writeFrame(dynamic_frame_or_dfc, info)

        elif isinstance(dynamic_frame_or_dfc, DynamicFrameCollection):
            res_frames = [self.writeFrame(frame)
                          for frame in dynamic_frame_or_dfc.values()]
            return DynamicFrameCollection(res_frames, self._sql_ctx)

        else:
            raise TypeError("dynamic_frame_or_dfc must be an instance of"
                            "DynamicFrame or DynamicFrameCollection. Got "
                            + str(type(dynamic_frame_or_dfc)))