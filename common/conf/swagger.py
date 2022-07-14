#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2021/6/16


from drf_yasg.inspectors import SwaggerAutoSchema

class CustomSwaggerAutoSchema(SwaggerAutoSchema):
    def get_tags(self, operation_keys=None):
        tags = super().get_tags(operation_keys)


        if "api" in tags and operation_keys:
            #  `operation_keys` 内容像这样 ['v1', 'prize_join_log', 'create']
            tags[0] = operation_keys[1]
        if not tags:
            tags = [operation_keys[0]]
        if hasattr(self.view, "swagger_tags"):
            tags = self.view.swagger_tags

        return tags


class CustomSwaggerAutoSchemaBase(SwaggerAutoSchema):
    def get_tags(self, operation_keys=None):
        operation_keys = operation_keys or self.operation_keys

        tags = self.overrides.get('tags')
        if not tags:
            tags = [operation_keys[0]]
        if hasattr(self.view, "swagger_tags"):
            tags = self.view.swagger_tags

        return tags
