#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2021/9/7

"""
用于封装了自定义的用户鉴权验证器、用户使用用户名、手机号码、邮箱进行登录获取用户token凭证
"""

from rest_framework import status, HTTP_HEADER_ENCODING
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import ParseError
from rest_framework_simplejwt.authentication import JWTAuthentication

from common.main import md5
from apps.user.models import User


class UserLoginAuth(BaseAuthentication):


    def authenticate(self, request):
        # 获取用户的token
        get_token = request.META.get('HTTP_TOKEN')

        # 进行验证token是否过期

        if get_token:
            user = User.objects.filter(token=get_token).first()
            print(user.username)
            # 验证token是否有效
            # isToken = certify_token(key=user.username, token=get_token)
            # if isToken:
            return (user, None)
            # else:
            #     ParseError.status_code = status.HTTP_403_FORBIDDEN
            #     raise ParseError({"code": 1, "message": "token 已失效"})
            #
        else:
            # 添加自定义的http响应码
            ParseError.status_code = status.HTTP_400_BAD_REQUEST
            raise ParseError({"code": 1, "message": "token不能为空"})

    def authenticate_header(self, request):
        pass


# 自定义得到token校验
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework import serializers

class UserTokenAuth(ModelBackend):
    """
    获取token身份凭证
    """
    def authenticate(self, request, **kwargs):
        """

        """
        # 查询用户
        user = User.objects.filter(Q(username=kwargs["username"]) | Q(email=kwargs["username"]) | Q(phone=kwargs["username"])).first()
        user_pwd = None
        try:
            # 可能查询不出结果、进行捕捉异常
            user_pwd = user.password
        except:
            raise serializers.ValidationError({'msg': '用户没有注册'})

        # 进行判断密码是否正确
        if md5(kwargs["password"]) == user_pwd :
            # 进行验证该用户是否是被禁用
            if user.status == 0 :
                ParseError.status_code = status.HTTP_400_BAD_REQUEST
                raise serializers.ValidationError({'msg': '用户被禁用'})
            # 进行验证该用户是不是管理员
            # if user.is_staff != 1 or user.is_superuser != 1:
            #     ParseError.status_code = status.HTTP_400_BAD_REQUEST
            #     raise serializers.ValidationError({'msg': '你不是管理员'})
            else:
                return user
        else:
            # 如果不想密码登录也可以验证码在这里写
            # 这里做验证码的操作
            # ParseError.status_code = status.HTTP_400_BAD_REQUEST
            # return ()
            raise serializers.ValidationError({'code':1,'msg': '密码错误',"message":1000})







class JWTUserToken(JWTAuthentication):
    """
    对JWTAuthentication 中的token认证相对应的api进行重写
    """
    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            return None

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)

        return self.get_user(validated_token), validated_token

    def get_header(self, request):
        """

        """
        header = request.META.get("HTTP_TOKEN")
        header_join = f"stack_note {header}"

        if isinstance(header_join, str):
            # Work around django test client oddness
            header = header_join.encode(HTTP_HEADER_ENCODING)

        return header


