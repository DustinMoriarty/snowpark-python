#
# Copyright (c) 2012-2024 Snowflake Computing Inc. All rights reserved.
#

# Licensed to Modin Development Team under one or more contributor license agreements.
# See the NOTICE file distributed with this work for additional information regarding
# copyright ownership.  The Modin Development Team licenses this file to you under the
# Apache License, Version 2.0 (the "License"); you may not use this file except in
# compliance with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific language
# governing permissions and limitations under the License.

# Code in this file may constitute partial or total reimplementation, or modification of
# existing code originally distributed by the Modin project, under the Apache License,
# Version 2.0.

"""Module houses default DataFrame functions builder class."""

import pandas

from snowflake.snowpark.modin.core.dataframe.algebra.default2pandas.default import (
    DefaultMethod,
)

# from modin.utils import _inherit_docstrings
from snowflake.snowpark.modin.utils import _inherit_docstrings


@_inherit_docstrings(DefaultMethod)
class DataFrameDefault(DefaultMethod):
    DEFAULT_OBJECT_TYPE = pandas.DataFrame
