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

class ResolveChoice(GlueTransform):
    def __call__(self, frame, specs=None, choice="", database=None, table_name=None, transformation_ctx="", info="", stageThreshold=0, totalThreshold=0, catalog_id=None):
        return frame.resolveChoice(specs, choice, database, table_name, transformation_ctx, info, stageThreshold, totalThreshold, catalog_id)

    @classmethod
    def describeArgs(cls):
        arg1 = {"name": "frame",
                "type": "DynamicFrame",
                "description": "DynamicFrame to transform",
                "optional": False,
                "defaultValue": None}
        arg2 = {"name": "specs",
                "type": "List",
                "description": "List of specs (path, action)",
                "optional": True,
                "defaultValue": None}
        arg3 = {"name": "choice",
                "type": "String",
                "description": "resolve choice option",
                "optional": True,
                "defaultValue": ""}
        arg4 = {"name": "database",
                "type": "String",
                "description": "Glue catalog database name, required for MATCH_CATALOG choice",
                "optional": True,
                "defaultValue": ""}
        arg5 = {"name": "table_name",
                "type": "String",
                "description": "Glue catalog table name, required for MATCH_CATALOG choice",
                "optional": True,
                "defaultValue": ""}
        arg6 = {"name": "transformation_ctx",
                "type": "String",
                "description": "A unique string that is used to identify stats / state information",
                "optional": True,
                "defaultValue": ""}
        arg7 = {"name": "info",
                "type": "String",
                "description": "Any string to be associated with errors in the transformation",
                "optional": True,
                "defaultValue": "\"\""}
        arg8 = {"name": "stageThreshold",
                "type": "Integer",
                "description": "Max number of errors in the transformation until processing will error out",
                "optional": True,
                "defaultValue": "0"}
        arg9 = {"name": "totalThreshold",
                "type": "Integer",
                "description": "Max number of errors total until processing will error out.",
                "optional": True,
                "defaultValue": "0"}
        arg10 = {"name": "catalog_id",
                "type": "String",
                "description": "Catalog id for match_catalog id.",
                "optional": True,
                "defaultValue": "accountId"}

        return [arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10]

    @classmethod
    def describeTransform(cls):
        return "Resolve choice type in this DynamicFrame."

    @classmethod
    def describeErrors(cls):
        return []

    @classmethod
    def describeReturn(cls):
        return {"type": "DynamicFrame",
                "description": "DynamicFrame after resolving choice type."}
