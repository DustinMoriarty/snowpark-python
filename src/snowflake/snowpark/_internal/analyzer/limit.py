#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
#

from snowflake.snowpark._internal.plans.logical.logical_plan import LogicalPlan
from snowflake.snowpark._internal.sp_expressions import Expression as SPExpression


class Limit(LogicalPlan):
    def __init__(self, limit_expr: SPExpression, child: LogicalPlan):
        super().__init__()
        self.limit_expr = limit_expr
        self.child = child
        self.children = [child]
