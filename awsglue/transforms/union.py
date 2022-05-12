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

from awsglue.transforms import GlueTransform

class Union(GlueTransform):
    def __call__(self, frame1, frame2, transformation_ctx = "",
                 info = "", stageThreshold = 0, totalThreshold = 0):
        return frame1.union(mappings, case_sensitive)

    @classmethod
    def describeArgs(cls):
        arg1 = {"name": "frame1",
                "type": "DynamicFrame",
                "description": "First DynamicFrame to union.",
                "optional": False,
                "defaultValue": None}
        arg2 = {"name": "frame2",
                "type": "DynamicFrame",
                "description": "Second DynamicFrame to union.",
                "optional": False,
                "defaultValue": None}
        arg3 = {"name": "transformation_ctx",
                "type": "String",
                "description": "A unique string that is used to identify stats / state information",
                "optional": True,
                "defaultValue": ""}
        arg4 = {"name": "info",
                "type": "String",
                "description": "Any string to be associated with errors in the transformation",
                "optional": True,
                "defaultValue": "\"\""}
        arg5 = {"name": "stageThreshold",
                "type": "Integer",
                "description": "Max number of errors in the transformation until processing will error out",
                "optional": True,
                "defaultValue": "0"}
        arg6 = {"name": "totalThreshold",
                "type": "Integer",
                "description": "Max number of errors total until processing will error out.",
                "optional": True,
                "defaultValue": "0"}

        return [arg1, arg2, arg3, arg4, arg5, arg6]

    @classmethod
    def describeTransform(cls):
        return "Union two DynamicFrames."

    @classmethod
    def describeErrors(cls):
        return []

    @classmethod
    def describeReturn(cls):
        return {"type": "DynamicFrame",
                "description": "DynamicFrame containing all records from both input DynamicFrames."}
