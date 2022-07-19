

#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2021/9/7
from django.db import models


# Create your models here.



from apps.user.models import Filesave

# 动态导航模型
class Nav(models.Model):
    id = models.CharField(primary_key=True, max_length=40, verbose_name='id')
    title = models.CharField( max_length=8, verbose_name='标题')
    path = models.CharField(max_length=20, verbose_name='路由路径')
    description = models.CharField(null=True, max_length=40, verbose_name='描述')
    createTime = models.DateTimeField(null=True, max_length=1, verbose_name='创建时间')
    updateTime = models.DateTimeField(null=True, max_length=1, verbose_name='修改时间')
    deleteTime = models.DateTimeField(null=True, max_length=1, verbose_name='删除时间')
    sort = models.IntegerField(verbose_name='排序',default=0)
    isDelete = models.IntegerField(null=True, default=0, verbose_name='删除状态')
    # 0 为不删除、1为删除	逻辑删除标记
    isShow = models.IntegerField(null=True, default=1, verbose_name='显示状态')
    # 	1 为显示、0为不显示	显示状态
    create_by = models.CharField(null=True, max_length=20, verbose_name='创建人')
    icon = models.ForeignKey(Filesave, null=True, on_delete=models.SET_NULL, verbose_name='文件id')


    def __str__(self):
          # 在该模型被关联是默认显示的字段
        return self.id

    class Meta:
        #   自定义表名
        db_table = 'stack_index_nav'
        # 表备注
        verbose_name_plural = "导航表"
        verbose_name = verbose_name_plural


# banner 模型
class Banner(models.Model):
    id = models.CharField(primary_key=True, max_length=40, verbose_name='id')
    title = models.CharField( max_length=20, verbose_name='标题')
    path = models.CharField(null=True,max_length=40, verbose_name='跳转路径')
    description = models.CharField(null=True, max_length=40, verbose_name='描述')
    createTime = models.DateTimeField(null=True, max_length=1, verbose_name='创建时间')
    updateTime = models.DateTimeField(null=True, max_length=1, verbose_name='修改时间')
    deleteTime = models.DateTimeField(null=True, max_length=1, verbose_name='删除时间')
    sort = models.IntegerField(verbose_name='排序',default=0)
    isDelete = models.IntegerField(null=True, default=0, verbose_name='删除状态')
    # 0 为删除、1为未删除	逻辑删除标记
    isShow = models.IntegerField(null=True, default=0, verbose_name='显示状态')
    # 	1 为显示、0为不显示	显示状态
    create_by = models.CharField(null=True, max_length=20, verbose_name='创建人')
    file = models.ForeignKey(Filesave, null=True, on_delete=models.SET_NULL, verbose_name='文件id')


    def __str__(self):
          # 在该模型被关联是默认显示的字段
        return self.id

    class Meta:
        #   自定义表名
        db_table = 'stack_index_banner'
        # 表备注
        verbose_name_plural = "banner表"
        verbose_name = verbose_name_plural



# 个人动态

from apps.article.models import Classify,User
class UserDynamic(models.Model):
    id = models.CharField(primary_key=True, max_length=20, verbose_name='id')
    title = models.CharField(null=True, max_length=40, verbose_name='标题')
    createTime = models.DateTimeField(null=True, max_length=0, verbose_name='创建时间')
    updateTime = models.DateTimeField(null=True, max_length=0, verbose_name='修改时间')
    deleteTime = models.DateTimeField(null=True, max_length=0, verbose_name='删除时间')
    # 文章 0-标签 1-分类 2-组织 3
    type = models.IntegerField(null=True, verbose_name='类型')

    # 点赞 0-发布 1-收藏 2-关注 3
    dy_type= models.IntegerField(null=True, verbose_name='动态类型')
    status = models.IntegerField(null=True, default=1, verbose_name='用户状态')
    # 1 正常 0被禁用	状态
    isDelete = models.IntegerField(null=True, default=0, verbose_name='删除状态')
    # 1 为删除、0为未删除	逻辑删除标记
    isShow = models.IntegerField(null=True, default=0, verbose_name='显示状态')
    # 	0 为显示、1为不显示	显示状态
    create_by = models.CharField(null=True, max_length=20, verbose_name='创建人')
    classify = models.ForeignKey(Classify, null=True, on_delete=models.SET_NULL, verbose_name='文章分类id')
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name='用户id')

    # 认证模型需要添加该属性
    # objects = UserManager()
    def __str__(self):
          # 在该模型被关联是默认显示的字段
        return self.id

    class Meta:
        #   自定义表名
        db_table = 'stack_user_dynamic'
        # 表备注
        verbose_name_plural = "用户表"
        verbose_name = verbose_name_plural
