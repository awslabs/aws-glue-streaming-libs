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

from py4j.java_gateway import java_import
from pyspark.sql.dataframe import DataFrame

class ApplyMapping():
    @staticmethod
    def apply(frame, mappings):
        jvm = frame.sql_ctx._jvm

        def _to_java_mapping(mapping_tup):
            if not isinstance(mapping_tup, tuple):
                raise TypeError("Mapping must be specified as a tuple. Got " +
                                mapping_tup)

            tup2 = jvm.scala.Tuple2
            tup3 = jvm.scala.Tuple3
            tup4 = jvm.scala.Tuple4

            if len(mapping_tup) == 2:
                return tup2.apply(mapping_tup[0], mapping_tup[1])
            elif len(mapping_tup) == 3:
                return tup3.apply(mapping_tup[0], mapping_tup[1], mapping_tup[2])
            elif len(mapping_tup) == 4:
                return tup4.apply(mapping_tup[0], mapping_tup[1], mapping_tup[2], mapping_tup[3])
            else:
                raise ValueError("Mapping tuple must be of length 2, 3, or 4"
                                 "Got tuple of length " + str(len(mapping_tup)))

        if isinstance(mappings, tuple):
            mappings = [mappings]

        mappings_seq = jvm.PythonUtils.toSeq([_to_java_mapping(m) for m in mappings])

        java_import(jvm, "com.amazonaws.services.glue.dataframeTransforms.ApplyMapping")

        return DataFrame(jvm.ApplyMapping.apply(frame._jdf, mappings_seq), frame.sql_ctx)

    @classmethod
    def describeArgs(cls):
        arg1 = {"name": "frame",
                "type": "DataFrame",
                "description": "DataFrame to transform",
                "optional": False,
                "defaultValue": None}
        arg2 = {"name": "mappings",
                "type": "DataFrame",
                "description": "List of mapping tuples (source col, source type, target col, target type)",
                "optional": False,
                "defaultValue": None}

        return [arg1, arg2]

    @classmethod
    def describeTransform(cls):
        return "Apply a declarative mapping to this DataFrame."

    @classmethod
    def describeErrors(cls):
        return []

    @classmethod
    def describeReturn(cls):
        return {"type": "DataFrame",
                "description": "DataFrame after applying mappings."}

