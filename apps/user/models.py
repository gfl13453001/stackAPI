#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2021/9/7

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


# 文件模型

class Filesave(models.Model):
    id = models.CharField(primary_key=True, max_length=40, verbose_name='id')
    fileType = models.CharField(max_length=80, verbose_name='文件类型')
    fileName = models.CharField(max_length=80, verbose_name='名称')
    # upload_to 上传图片/文件存放路径
    #  图片保存路经%Y%M文件夹名称为日期
    createTime = models.CharField(max_length=10, verbose_name='时间')
    deleteTime = models.CharField(max_length=10, verbose_name='删除时间')

    isDelete = models.IntegerField(default=1, verbose_name='逻辑删除标记')
    # 0 为删除、1为未删除
    url = models.CharField(max_length=200, verbose_name='在线url')
    size = models.IntegerField(null=True, verbose_name='文件大小')


    def __str__(self):
        return self.id

    class Meta:
        db_table = 'stack_file'
        verbose_name_plural = "文件上传"


class User(AbstractUser):
    id = models.CharField(primary_key=True, max_length=20, verbose_name='id')
    # username = models.CharField(max_length=20, verbose_name='用户名',unique=True)
    # USERNAME_FIELD = "username"
    # REQUIRED_FIELDS = "username"
    nickname = models.CharField(null=True, max_length=20, verbose_name='昵称')

    sex = models.IntegerField(null=True,verbose_name='性别', default=0)
    # 0保密 1男 2女 default 默认值
    age = models.IntegerField(null=True, verbose_name='年龄', default=0)
    phone = models.CharField(max_length=11, verbose_name='电话')
    role = models.CharField(null=True, max_length=10, verbose_name='用户角色', default="MEMBER")
    # member MEMBER 普通会员
    introduce = models.CharField(null=True, max_length=80, verbose_name='介绍')
    signin = models.CharField(null=True, max_length=10, verbose_name='签名')
    tag = models.CharField(null=True, max_length=10, verbose_name='标签')
    createTime = models.CharField(null=True, max_length=10, verbose_name='创建时间')
    updateTime = models.CharField(null=True, max_length=10, verbose_name='修改时间')
    deleteTime = models.CharField(null=True, max_length=10, verbose_name='删除时间')
    recentlyLoginSite = models.CharField(null=True, max_length=20, verbose_name='最近登录地点')
    token = models.CharField(null=True, max_length=80, verbose_name='token')
    ip = models.CharField(null=True, max_length=20, verbose_name='登录ip')
    status = models.IntegerField(null=True, default=1, verbose_name='用户状态')
    # 1 正常 0被禁用	状态
    isDelete = models.IntegerField(null=True, default=0, verbose_name='删除状态')
    # 1 为删除、0为未删除	逻辑删除标记
    isShow = models.IntegerField(null=True, default=0, verbose_name='显示状态')
    # 	0 为显示、1为不显示	显示状态
    create_by = models.CharField(null=True, max_length=20, verbose_name='创建人')
    picturePath = models.ForeignKey(Filesave, null=True, on_delete=models.SET_NULL, verbose_name='文件id')

    # 认证模型需要添加该属性
    # objects = UserManager()
    def __str__(self):
          # 在该模型被关联是默认显示的字段
        return self.id

    class Meta:
        #   自定义表名
        db_table = 'stack_user'
        # 表备注
        verbose_name_plural = "用户表"
        verbose_name = verbose_name_plural




