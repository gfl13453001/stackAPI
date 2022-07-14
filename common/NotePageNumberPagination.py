#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2021/9/15
from rest_framework.pagination import PageNumberPagination


class LargeResultsSetPagination(PageNumberPagination):
    """
    自定义分页器
    """
    # page_size = 1000
    page_size_query_param = 'size'
    page_query_param = "page"
    max_page_size = 100
