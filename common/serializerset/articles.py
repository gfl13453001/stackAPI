#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2021/9/13
import datetime
import time

from rest_framework import serializers

from apps.article.models import (Classify, Article)
from apps.user.models import User, Filesave
from common.main import getID


class ClassifySerializerModels(serializers.ModelSerializer):
    id = serializers.CharField(required=False,max_length=40,min_length=40,label="id",read_only=True)
    name = serializers.CharField(min_length=2,max_length=8, label='分类名称',error_messages={
        "min_length":"至少2字符","max_length":"最大只能8字符"
    })

    description = serializers.CharField(required=False,max_length=40, label='描述',error_messages={
        "min_length":"至少2字符","max_length":"最大只能8字符"
    })
    createTime = serializers.CharField(required=False, max_length=10, label='创建时间',default=int(time.time()))
    updateTime = serializers.CharField(required=False, max_length=10, label='修改时间')
    deleteTime = serializers.CharField(required=False, max_length=10, label='删除时间')
    sort = serializers.IntegerField(required=False,label='排序',default=0)
    type = serializers.IntegerField(required=False,label='分类类型',default=0)
    isDelete = serializers.IntegerField(required=False, default=0, label='删除状态',)
    # 0 为删除、1为未删除	逻辑删除标记
    isShow = serializers.IntegerField(required=False, default=0, label='显示状态')
    # 	0 为显示、1为不显示	显示状态
    create_by = serializers.CharField(required=False, max_length=20, label='创建人',)


    class Meta:
        model = Classify
        depth = 2
        exclude = ()


    def create(self, validated_data):
        """

        """

        validated_data["id"] = getID(index=40)

        try:
            return Classify.objects.create(**validated_data)

        except:
            return serializers.ValidationError("接口异常")


    def update(self, instance, validated_data):
        print("原值",instance,"修改值",validated_data)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.updateTime = int(time.time())
        instance.sort = validated_data.get('sort', instance.sort)
        instance.isDelete = validated_data.get('isDelete', instance.isDelete)
        instance.isShow = validated_data.get('isShow', instance.isShow)
        instance.create_by = validated_data.get('create_by', instance.create_by)
        instance.save()
        return validated_data

class ArticleSerializerModels(serializers.ModelSerializer):
    id = serializers.CharField(required=False,max_length=40,min_length=40,label="id",read_only=True)
    title = serializers.CharField(min_length=2,max_length=60, label='分类名称',error_messages={
        "min_length":"至少2字符","max_length":"最大只能60字符"
    })

    description = serializers.CharField(required=False,max_length=160, label='描述',error_messages={
        "min_length":"至少2字符","max_length":"最大只能8字符"
    })
    content = serializers.CharField(required=False,min_length=4,label='描述',error_messages={
        "min_length":"至少2字符","max_length":"最大只能5000字符"
    })
    createTime = serializers.CharField(required=False, max_length=10, label='创建时间',default=datetime.datetime.now())
    updateTime = serializers.CharField(required=False, max_length=10, label='修改时间')
    deleteTime = serializers.CharField(required=False, max_length=10, label='删除时间')
    sort = serializers.IntegerField(required=False,label='排序',default=0)
    type = serializers.IntegerField(required=False,label='分类类型',default=0)
    isDelete = serializers.IntegerField(required=False, default=0, label='删除状态',)
    # 0 为删除、1为未删除	逻辑删除标记
    isShow = serializers.IntegerField(required=False, default=0, label='显示状态')
    # 	0 为显示、1为不显示	显示状态
    create_by = serializers.CharField(required=False, max_length=20, label='创建人',)
    check = serializers.IntegerField(required=False,  label='审核',default=2)
    img = serializers.CharField(required=True, label='封面',)
    userid = serializers.CharField(required=False, label='作者',)
    classify = serializers.CharField(required=True,error_messages={

    }, label='分类',)


    class Meta:
        model = Article
        depth = 2
        exclude = ()


    def create(self, validated_data):
        """

        """
        print(validated_data)
        validated_data["id"] = getID(index=10)
        validated_data["img_id"] = validated_data["img"]
        validated_data["classify_id"] = validated_data["classify"]
        validated_data["user_id"] = validated_data["userid"]

        try:

            if User.objects.filter(id=validated_data["userid"]) and Classify.objects.filter(
                    id=validated_data["classify"]) and Filesave.objects.filter(id=validated_data["img"]):
                validated_data.pop("img")
                validated_data.pop("classify")
                validated_data.pop("userid")
                return Article.objects.create(**validated_data)

            return 1

        except:
            return serializers.ValidationError("接口异常")


    def update(self, instance, validated_data):
        print("原值",instance,"修改值",validated_data)

        try:
            instance.title = validated_data.get('title', instance.title)
            instance.description = validated_data.get('description', instance.description)
            instance.content = validated_data.get('content', instance.content)
            instance.updateTime = int(time.time())
            instance.sort = validated_data.get('sort', instance.sort)
            instance.type = validated_data.get('type', instance.type)
            instance.isDelete = validated_data.get('isDelete', instance.isDelete)
            instance.isShow = validated_data.get('isShow', instance.isShow)
            instance.check = validated_data.get('check', instance.check)
            instance.img = validated_data.get('img', instance.img)
            instance.user = validated_data.get('user', instance.user)
            instance.classify = validated_data.get('classify', instance.classify)
            instance.save()
            return validated_data
        except:
            return 1



class ArticleListSerializerModels(serializers.ModelSerializer):
    id = serializers.CharField(required=False,max_length=40,min_length=40,label="id",read_only=True)
    title = serializers.CharField(min_length=2,max_length=60, label='分类名称',error_messages={
        "min_length":"至少2字符","max_length":"最大只能8字符"
    })

    description = serializers.CharField(required=False,max_length=160, label='描述',error_messages={
        "min_length":"至少2字符","max_length":"最大只能8字符"
    })
    content = serializers.CharField(required=False,min_length=4,label='描述',error_messages={
        "min_length":"至少2字符","max_length":"最大只能5000字符"
    })
    createTime = serializers.CharField(required=False, max_length=10, label='创建时间',default=datetime.datetime.now())
    updateTime = serializers.CharField(required=False, max_length=10, label='修改时间')
    deleteTime = serializers.CharField(required=False, max_length=10, label='删除时间')
    sort = serializers.IntegerField(required=False,label='排序',default=0)
    type = serializers.IntegerField(required=False,label='分类类型',default=0)
    isDelete = serializers.IntegerField(required=False, default=0, label='删除状态',)
    # 0 为删除、1为未删除	逻辑删除标记
    isShow = serializers.IntegerField(required=False, default=0, label='显示状态')
    # 	0 为显示、1为不显示	显示状态
    create_by = serializers.CharField(required=False, max_length=20, label='创建人',)
    check = serializers.IntegerField(required=False,  label='审核',default=2)
    # img = serializers.CharField(required=True, label='封面',)
    # userid = serializers.CharField(required=False, label='作者',)
    # classify = serializers.CharField(required=True,error_messages={

    # }, label='分类',)


    class Meta:
        model = Article
        depth = 2
        exclude = ()


    def create(self, validated_data):
        """

        """
        print(validated_data)
        validated_data["id"] = getID(index=10)
        validated_data["img_id"] = validated_data["img"]
        validated_data["classify_id"] = validated_data["classify"]
        validated_data["user_id"] = validated_data["userid"]

        try:

            if User.objects.filter(id=validated_data["userid"]) and Classify.objects.filter(
                    id=validated_data["classify"]) and Filesave.objects.filter(id=validated_data["img"]):
                validated_data.pop("img")
                validated_data.pop("classify")
                validated_data.pop("userid")
                return Article.objects.create(**validated_data)

            return 1

        except:
            return serializers.ValidationError("接口异常")


    def update(self, instance, validated_data):
        print("原值",instance,"修改值",validated_data)

        try:
            instance.title = validated_data.get('title', instance.title)
            instance.description = validated_data.get('description', instance.description)
            instance.content = validated_data.get('content', instance.content)
            instance.updateTime = int(time.time())
            instance.sort = validated_data.get('sort', instance.sort)
            instance.type = validated_data.get('type', instance.type)
            instance.isDelete = validated_data.get('isDelete', instance.isDelete)
            instance.isShow = validated_data.get('isShow', instance.isShow)
            instance.check = validated_data.get('check', instance.check)
            instance.img = validated_data.get('img', instance.img)
            instance.user = validated_data.get('user', instance.user)
            instance.classify = validated_data.get('classify', instance.classify)
            instance.save()
            return validated_data
        except:
            return 1



class ArticleSerializerDetailModels(serializers.ModelSerializer):

    class Meta:
        model = Article
        depth = 2
        fields = '__all__'



