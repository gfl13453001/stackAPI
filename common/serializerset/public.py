#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2021/9/9
import time

from rest_framework import serializers

from common.main import getID
from apps.public.models import (Nav, Banner)
from apps.user.models import Filesave


class NavSerializerModels(serializers.ModelSerializer):
    id = serializers.CharField(required=False,max_length=40,min_length=40,label="id",read_only=True)
    title = serializers.CharField(min_length=2,max_length=8, label='标题',error_messages={
        "min_length":"至少2字符","max_length":"最大只能8字符"
    })
    path = serializers.CharField(max_length=20, label='路由路径',error_messages={
        "min_length":"至少2字符","max_length":"最大只能8字符"
    })
    description = serializers.CharField(required=False,max_length=40, label='描述',error_messages={
        "min_length":"至少2字符","max_length":"最大只能8字符"
    })
    createTime = serializers.CharField(required=False, max_length=10, label='创建时间',default=int(time.time()))
    updateTime = serializers.CharField(required=False, max_length=10, label='修改时间')
    deleteTime = serializers.CharField(required=False, max_length=10, label='删除时间')
    sort = serializers.IntegerField(required=False,label='排序',default=0)
    isDelete = serializers.IntegerField(required=False, default=0, label='删除状态',)
    # 0 为删除、1为未删除	逻辑删除标记
    isShow = serializers.IntegerField(required=False, default=0, label='显示状态')
    # 	0 为显示、1为不显示	显示状态
    create_by = serializers.CharField(required=False, max_length=20, label='创建人',)
    icon_id = serializers.CharField(required=False,  label='文件id',write_only=True)


    class Meta:
        model = Nav
        depth = 2
        exclude = ()


    def create(self, validated_data):
        """
        用于创建菜单导航
        """
        try:
            validated_data["icon_id"] = validated_data["icon_id"][0].id
        except:
            pass
        validated_data["id"] = getID(index=40)

        try:
            return Nav.objects.create(**validated_data)

        except:
            return serializers.ValidationError("接口异常")


    def update(self, instance, validated_data):
        print("原值",instance,"修改值",validated_data)
        instance.title = validated_data.get('title', instance.title)
        instance.path = validated_data.get('path', instance.path)
        instance.description = validated_data.get('description', instance.description)
        instance.updateTime = int(time.time())
        instance.sort = validated_data.get('sort', instance.sort)
        instance.isDelete = validated_data.get('isDelete', instance.isDelete)
        instance.isShow = validated_data.get('isShow', instance.isShow)
        instance.create_by = validated_data.get('create_by', instance.create_by)
        instance.icon = validated_data.get('icon_id', instance.icon_id)
        instance.save()
        return validated_data





class BannerSerializerModels(serializers.ModelSerializer):
    id = serializers.CharField(required=False,max_length=40,min_length=40,label="id",read_only=True)
    title = serializers.CharField(min_length=2,max_length=8, label='标题',error_messages={
        "min_length":"至少2字符","max_length":"最大只能8字符"
    })
    path = serializers.CharField(max_length=20, label='路由路径',error_messages={
        "min_length":"至少2字符","max_length":"最大只能20字符"
    })
    description = serializers.CharField(required=False,max_length=40, label='描述',error_messages={
        "min_length":"至少2字符","max_length":"最大只能8字符"
    })
    createTime = serializers.CharField(required=False, max_length=10, label='创建时间',default=int(time.time()))
    updateTime = serializers.CharField(required=False, max_length=10, label='修改时间')
    deleteTime = serializers.CharField(required=False, max_length=10, label='删除时间')
    sort = serializers.IntegerField(required=False,label='排序',default=0)
    isDelete = serializers.IntegerField(required=False, default=0, label='删除状态',)
    # 0 为删除、1为未删除	逻辑删除标记
    isShow = serializers.IntegerField(required=False, default=0, label='显示状态')
    # 	0 为显示、1为不显示	显示状态
    create_by = serializers.CharField(required=False, max_length=20, label='创建人',)
    file_id = serializers.CharField(required=False,  label='banner 图片',write_only=True)


    class Meta:
        model = Banner
        depth = 2
        exclude = ()


    def create(self, validated_data):
        """
        用于创建菜单导航
        """
        try:
            validated_data["icon_id"] = validated_data["icon_id"][0].id
        except:
            pass
        validated_data["id"] = getID(index=40)

        try:
            return Banner.objects.create(**validated_data)

        except:
            return serializers.ValidationError("接口异常")


    def update(self, instance, validated_data):
        print("原值",instance,"修改值",validated_data)
        instance.title = validated_data.get('title', instance.title)
        instance.path = validated_data.get('path', instance.path)
        instance.description = validated_data.get('description', instance.description)
        instance.updateTime = int(time.time())
        instance.sort = validated_data.get('sort', instance.sort)
        instance.isDelete = validated_data.get('isDelete', instance.isDelete)
        instance.isShow = validated_data.get('isShow', instance.isShow)
        instance.create_by = validated_data.get('create_by', instance.create_by)
        instance.file_id = validated_data.get('icon_id', instance.file_id)
        instance.save()
        return validated_data




class UploadFIleSerializerModels(serializers.ModelSerializer):
    id = serializers.CharField(max_length=40, label='id')
    fileType = serializers.CharField(max_length=80, label='文件类型')
    fileName = serializers.CharField(max_length=80, label='文件名称')
    createTime = serializers.CharField(required=False, max_length=10, label='创建时间',default=int(time.time()))
    deleteTime = serializers.CharField(required=False, max_length=10, label='删除时间')
    isDelete = serializers.IntegerField(required=False, default=0, label='删除状态',)
    # 0 为删除、1为未删除	逻辑删除标记
    # 	0 为显示、1为不显示	显示状态
    url = serializers.CharField(required=False, max_length=200, label='url',)
    size = serializers.CharField(required=False,label="文件大小")


    class Meta:
        model = Filesave
        exclude = ()


    def create(self, validated_data):
        """
        用于创建文件
        """

        try:
            return Filesave.objects.create(**validated_data)
        except:
            return serializers.ValidationError("接口异常")




class testSerializerModels(serializers.Serializer):
    # id = serializers.CharField(max_length=40, label='id')
    # fileType = serializers.CharField(max_length=80, label='文件类型')
    # fileName = serializers.CharField(max_length=80, label='文件名称')
    # createTime = serializers.CharField(required=False, max_length=10, label='创建时间',default=int(time.time()))
    # deleteTime = serializers.CharField(required=False, max_length=10, label='删除时间')
    # isDelete = serializers.IntegerField(required=False, default=0, label='删除状态',)
    # # 0 为删除、1为未删除	逻辑删除标记
    # # 	0 为显示、1为不显示	显示状态
    # url = serializers.CharField(required=False, max_length=200, label='url',)
    # size = serializers.CharField(required=False,label="文件大小")

    dataList = NavSerializerModels(read_only=True)


    class Meta:
        model = Filesave
        # exclude = ()







