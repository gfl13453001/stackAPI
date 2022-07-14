#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2021/9/9


from rest_framework import routers

class CustomRouter(routers.SimpleRouter):
    """
    自定义的动态路由生成类，用于动态生成viewset中detail=False的接口路由，且不生成DRF原生CURD接口默认生成的路由和detail=True的路由
    配合DRF的ModelViewSet实现CBV的接口
    """
    routes = [
        # Dynamically generated list routes. Generated using
        # @action(detail=False) decorator on methods of the viewset.
        routers.DynamicRoute(
            url=r'^{prefix}/{url_path}{trailing_slash}$',
            name='{basename}-{url_name}',
            detail=False,
            initkwargs={}
        ),
    ]
