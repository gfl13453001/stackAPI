#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2021/9/13
from django.urls import path
from rest_framework.routers import  SimpleRouter

from apps.article.views import (ArticleClassifyViewSet, CreateArticleViewSet, MyArticleViewSet, GetArticleViewSet,
                                ClassifyGetArticleViewSet)

router = SimpleRouter(trailing_slash=False,)
router.register(r'article/classify', ArticleClassifyViewSet, basename='文章分类',)
router.register(r'article', CreateArticleViewSet, basename='文章模块',)
router.register(r'article/user/list', MyArticleViewSet, basename='文章模块',)

urlpatterns = [
    path('article/list', GetArticleViewSet.as_view({"get": "list"}), name=''),
    path('article/classify/list', ClassifyGetArticleViewSet.as_view({"get": "list"}), name=''),
]
urlpatterns += router.urls
