#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2021/9/7
from random import Random

from rest_framework import serializers

from common.main import getID, md5
from apps.user.models import User
import time

class UserNameLoginSerializerModels(serializers.ModelSerializer):
    username = serializers.CharField(max_length=18,min_length=6,label="用戶名")
    password = serializers.CharField(max_length=18,min_length=6,label="密码")

    class Meta:
        model = User
        fields = ("username","password")


    def validate(self, data):
        """
        验证密码正确性
        """

        if User.objects.filter(username=data["username"]):

            if User.objects.filter(username=data["username"],password=data["password"]):
                return data
            else:
                raise serializers.ValidationError("用户名或密码错误")
        else:
            raise serializers.ValidationError("该用户不存在")






# class CreateUserSerializerModels(serializers.ModelSerializer):
#     user_name = Random().randint(1,999999)
#
#     id = serializers.CharField(required=False,max_length=40,min_length=40,label="id",read_only=True)
#     username = serializers.CharField(max_length=18,min_length=6,label="用戶名",error_messages={
#         "max_length":"最大18位","min_length":"最少需要6位",})
#     password = serializers.CharField(max_length=18,min_length=6,label="密码",error_messages={
#         "max_length":"最大18位","min_length":"最少需要6位",})
#     repwd = serializers.CharField(max_length=18,min_length=6,label="确认密码",write_only=True,error_messages={
#         "max_length":"最大18位","min_length":"最少需要6位",})
#     nickname = serializers.CharField(required=False, max_length=18, min_length=6,label="昵称",error_messages={
#         "max_length":"最大18位","min_length":"最少需要6位",},default="User_%06d"%user_name)
#     sex = serializers.IntegerField(required=False, label='性别', default=0)
#     # 0保密 1男 2女 default 默认值
#     age = serializers.IntegerField(required=False, label='年龄', default=0)
#     phone = serializers.CharField(required=False,max_length=11, label='电话',min_length=11,error_messages={
#         "max_length":"最大11位","min_length":"最少需要11位",})
#     introduce = serializers.CharField(required=False, max_length=80, label='介绍',error_messages={
#         "max_length":"最大80位","min_length":"最少需要10位",},default="这个人很懒，好像啥也没写~")
#     signin = serializers.CharField(required=False, max_length=10, label='签名')
#     # email = models.CharField(null=True, max_length=40, verbose_name='email')
#     tag = serializers.CharField(required=False, max_length=10, label='标签')
#     createTime = serializers.CharField(required=False, max_length=10, label='创建时间',default=int(time.time()))
#     updateTime = serializers.CharField(required=False, max_length=10, label='修改时间',)
#     deleteTime = serializers.CharField(required=False, max_length=10, label='删除时间',)
#     # last_login = models.CharField(null=True, max_length=10, verbose_name='最近登录时间')
#     recentlyLoginSite = serializers.CharField(required=False, max_length=20, label='最近登录地点')
#     token = serializers.CharField(required=False, max_length=80, label='token')
#     ip = serializers.CharField(required=False, max_length=20, label='登录ip')
#     status = serializers.IntegerField(required=False, default=0, label='用户状态')
#     # 0 正常 1被禁用	状态
#     isDelete = serializers.IntegerField(required=False, default=0, label='删除状态')
#     # 0 为删除、1为未删除	逻辑删除标记
#     isShow = serializers.IntegerField(required=False, default=0, label='显示状态')
#     # 	0 为显示、1为不显示	显示状态
#     # password = models.CharField(max_length=40, verbose_name='密码')
#     create_by = serializers.CharField(required=False, max_length=20, label='创建人')
#     picturePath = serializers.CharField(required=False, label='文件id')
#
#     class Meta:
#         model = User
#         exclude = ()
#
#
#
#     def validate(self, data):
#         """
#         验证密码正确性
#         """
#
#         print(data)
#
#         if User.objects.filter(username=data["username"]):
#             raise serializers.ValidationError({"msg":"用户已存在"})
#         else:
#             if data["password"] == data["repwd"]:
#                 return data
#             else:
#                 raise serializers.ValidationError({"msg":"二次密码不相同"})
#
#
#     def create(self, validated_data):
#         """
#         用于创建用户
#         """
#         validated_data["id"] = getID(index=40)
#         validated_data["password"] = md5(validated_data["password"])
#         validated_data.pop("repwd")
#         try:
#             print(666,validated_data)
#
#             return User.objects.create(**validated_data)
#         except:
#             return serializers.ValidationError("接口异常")
#
#
#     def delete(self, validated_data):
#         """
#         删除用户
#         """
#
#         return validated_data
#         # validated_data["id"] = getID(index=40)
#         # validated_data["password"] = md5(validated_data["password"])
#         # print(User.objects.filter(username=validated_data["username"]))
#         # try:
#         #     if User.objects.filter(username=validated_data["username"]):
#         #         print(1)
#         #         return Response({"message":"用户已存在"})
#         #     else:
#         #         return User.objects.create(**validated_data)
#         # except:
#         #     return serializers.ValidationError("接口异常")
#
#     def update(self, instance, validated_data):
#         print("原值",instance,"修改值",validated_data)
#         # print("原值",instance,"修改值",validated_data)
#         print("加密前",validated_data["password"])
#
#         validated_data["password"] = md5(validated_data["password"])
#         print("加密后", validated_data["password"])
#
#         instance.username = validated_data.get('username', instance.username)
#         instance.password = validated_data.get('password', instance.password)
#         instance.nickname = validated_data.get('nickname', instance.nickname)
#         instance.sex = validated_data.get('sex', instance.sex)
#         instance.age = validated_data.get('age', instance.age)
#         instance.phone = validated_data.get('phone', instance.phone)
#         instance.introduce = validated_data.get('introduce', instance.introduce)
#         instance.signin = validated_data.get('signin', instance.signin)
#         instance.tag = validated_data.get('tag', instance.tag)
#         instance.updateTime = int(time.time())
#         instance.recentlyLoginSite = validated_data.get('recentlyLoginSite', instance.recentlyLoginSite)
#         instance.ip = validated_data.get('ip', instance.ip)
#         instance.status = validated_data.get('status', instance.status)
#         instance.isDelete = validated_data.get('isDelete', instance.isDelete)
#         instance.save()
#         return validated_data
#
#

class UserInfoSerializerModels(serializers.ModelSerializer):

    class Meta:
        model = User
        depth = 2
        fields = '__all__'



class CreateUserSerializerModels(serializers.ModelSerializer):

    id = serializers.CharField(required=False,max_length=40,min_length=40,label="id",read_only=True)
    username = serializers.CharField(max_length=18,min_length=6,label="用戶名",error_messages={
        "max_length":"最大18位","min_length":"最少需要6位",})
    password = serializers.CharField(max_length=18,min_length=6,label="密码",error_messages={
        "max_length":"最大18位","min_length":"最少需要6位",})
    nickname = serializers.CharField(required=False, max_length=18, min_length=6,label="昵称",error_messages={
        "max_length":"最大18位","min_length":"最少需要6位",})
    sex = serializers.IntegerField(required=False, label='性别', default=0)
    # 0保密 1男 2女 default 默认值
    age = serializers.IntegerField(required=False, label='年龄', default=0)
    phone = serializers.CharField(required=False,max_length=11, label='电话',min_length=11,error_messages={
        "max_length":"最大11位","min_length":"最少需要11位",})
    introduce = serializers.CharField(required=False, max_length=80, label='介绍',error_messages={
        "max_length":"最大80位","min_length":"最少需要10位",})
    signin = serializers.CharField(required=False, max_length=10, label='签名')
    # email = models.CharField(null=True, max_length=40, verbose_name='email')
    tag = serializers.CharField(required=False, max_length=10, label='标签')
    createTime = serializers.CharField(required=False, max_length=10, label='创建时间',default=int(time.time()))
    updateTime = serializers.CharField(required=False, max_length=10, label='修改时间',)
    deleteTime = serializers.CharField(required=False, max_length=10, label='删除时间',)
    # last_login = models.CharField(null=True, max_length=10, verbose_name='最近登录时间')
    recentlyLoginSite = serializers.CharField(required=False, max_length=20, label='最近登录地点')
    token = serializers.CharField(required=False, max_length=80, label='token')
    ip = serializers.CharField(required=False, max_length=20, label='登录ip')
    status = serializers.IntegerField(required=False, default=0, label='用户状态')
    # 0 正常 1被禁用	状态
    isDelete = serializers.IntegerField(required=False, default=0, label='删除状态')
    # 0 为删除、1为未删除	逻辑删除标记
    isShow = serializers.IntegerField(required=False, default=0, label='显示状态')
    # 	0 为显示、1为不显示	显示状态
    # password = models.CharField(max_length=40, verbose_name='密码')
    create_by = serializers.CharField(required=False, max_length=20, label='创建人')
    # picturePath = serializers.PrimaryKeyRelatedField(required=False, many=True, label='文件id',queryset=User.objects.all())
    picturePath = serializers.CharField(required=False,)

    class Meta:
        model = User
        depth = 2
        exclude = ()




    # def validate(self, data):
    #     """
    #     验证密码正确性
    #     """
    #
    #     if User.objects.filter(username=data["username"]):
    #
    #         if User.objects.filter(username=data["username"],password=data["password"]):
    #             return data
    #         else:
    #             raise serializers.ValidationError("用户名或密码错误")
    #     else:
    #         raise serializers.ValidationError("该用户不存在")

    def create(self, validated_data):
        """
        用于创建用户
        """
        validated_data["id"] = getID(index=20)
        validated_data["password"] = md5(validated_data["password"])
        validated_data["is_superuser"] = 1
        validated_data["is_staff"] = 1
        validated_data["picturePath_id"] = validated_data["picturePath"]
        validated_data.pop("picturePath")
        print(validated_data)
        try:
            return User.objects.update_or_create(**validated_data)
        except:
            return serializers.ValidationError("接口异常")


    def delete(self, validated_data):
        """
        删除用户
        """
        print(validated_data)
        return validated_data
        # validated_data["id"] = getID(index=40)
        # validated_data["password"] = md5(validated_data["password"])
        # print(User.objects.filter(username=validated_data["username"]))
        # try:
        #     if User.objects.filter(username=validated_data["username"]):
        #         print(1)
        #         return Response({"message":"用户已存在"})
        #     else:
        #         return User.objects.create(**validated_data)
        # except:
        #     return serializers.ValidationError("接口异常")

    def update(self, instance, validated_data):
        print("原值",instance,"修改值",validated_data)
        # print("原值",instance,"修改值",validated_data)
        print("加密前",validated_data["password"])

        validated_data["password"] = md5(validated_data["password"])
        print("加密后", validated_data["password"])

        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.sex = validated_data.get('sex', instance.sex)
        instance.age = validated_data.get('age', instance.age)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.introduce = validated_data.get('introduce', instance.introduce)
        instance.signin = validated_data.get('signin', instance.signin)
        instance.tag = validated_data.get('tag', instance.tag)
        instance.updateTime = int(time.time())
        instance.recentlyLoginSite = validated_data.get('recentlyLoginSite', instance.recentlyLoginSite)
        instance.ip = validated_data.get('ip', instance.ip)
        instance.status = validated_data.get('status', instance.status)
        instance.isDelete = validated_data.get('isDelete', instance.isDelete)
        instance.save()
        return validated_data



