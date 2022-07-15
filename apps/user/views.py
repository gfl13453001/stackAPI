#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2021/9/7


# redis操作
from django_redis import get_redis_connection

# 数据缓存
# from django.core.cache import cache
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenViewBase)

# from common.NotePageNumberPagination import LargeResultsSetPagination
from common.serializerset.public import testSerializerModels
from common.serializerset.tokenSerializers import MyTokenObtainPairSerializer
from common.serializerset.user import (CreateUserSerializerModels, UserInfoSerializerModels)
from common.authenticationclass import JWTUserToken
from common.main import ResponseContent
from apps.user.models import User, Filesave

cache = get_redis_connection('default')


class UserLoginViewSet(TokenObtainPairView):
    """
    登录
    """
    swagger_tags = ["登录"]
    renderer_classes = [JSONRenderer]
    serializer_class = MyTokenObtainPairSerializer



# list() 提供一组数据
# retrieve() 提供单个数据
# create() 创建数据
# update() 保存数据 partial_update
# destory() 删除数据

class UserRegisterViewSet(ViewSet):

    """
    注册
    """
    # swagger 分类标签
    swagger_tags = ["注册"]
    # 渲染器
    renderer_classes = [JSONRenderer]
    # 权限控制器
    # permission_classes = [IsAuthenticated]
    # 认证器
    # authentication_classes = [JWTUserToken]
    # 版本控制器
    versioning_class = URLPathVersioning


    @swagger_auto_schema(
        operation_description="注册",
        # 配置接口的请求body、post请求数据是保存在body中的
        request_body=openapi.Schema(
            # 接口请求参数的类型、是一个对象类型、前端对应的是json类型
            type=openapi.TYPE_OBJECT,
            # 设置必须传入的参数
            required=['username', 'password','repwd'],
            # body中的参数选项
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING,description="用户名",default="admin"),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description="密码", default="123456"),
                'repwd': openapi.Schema(type=openapi.TYPE_STRING, description="确认密码", default="123456"),
                'nickname': openapi.Schema(type=openapi.TYPE_STRING, description="用戶名",),
                'sex': openapi.Schema(type=openapi.TYPE_NUMBER, description="性别",),
                'age': openapi.Schema(type=openapi.TYPE_NUMBER, description="年龄",),
                'phone': openapi.Schema(type=openapi.TYPE_STRING, description="手机号码",),
                'introduce': openapi.Schema(type=openapi.TYPE_STRING, description="介绍",),
                'signin': openapi.Schema(type=openapi.TYPE_STRING, description="签名",),
                'tag': openapi.Schema(type=openapi.TYPE_STRING, description="标签",),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description="email",),
                'status': openapi.Schema(type=openapi.TYPE_NUMBER, description="用户状态",default=0),
                'picturePath': openapi.Schema(type=openapi.TYPE_STRING, description="用户头像",default=0),
            },
        ),
        # 接口响应的具体内容
        responses={202: 'id not found'},
        # 进行给这个api备注、swagger ui上显示的内容
        operation_summary='注册'
    )

    def create(self, request, *args,**kwargs):
        # 添加用户
        user_data = request.data
        user_json = CreateUserSerializerModels(data=user_data)  # 必须明确data

        if user_json.is_valid():  # 校验

            if User.objects.filter(username=user_data["username"]):
                return Response(
                    ResponseContent(code=0, message="用户已存在").__dict__
                )

            else:
                print(user_json)
                user_json.save()  # 保存
                return Response(
                    ResponseContent(code=0, message="注册成功").__dict__
                )

        try:
            return Response(
                ResponseContent(code=1, message=user_json.errors["msg"][0]).__dict__
            )
        except:
            return Response(
                ResponseContent(code=1, message=user_json.errors).__dict__
            )

class AccountCenterViewSet(ViewSet):

    """
    账号中心
    """
    # swagger 分类标签
    swagger_tags = ["账号中心"]
    # 渲染器
    renderer_classes = [JSONRenderer]
    # 权限控制器
    permission_classes = [IsAuthenticated]
    # 认证器
    authentication_classes = [JWTUserToken]
    # 版本控制器
    versioning_class = URLPathVersioning


    @swagger_auto_schema(
        operation_description="获取我的个人信息",
        # 配置接口的请求body、post请求数据是保存在body中的
        request_body=openapi.Schema(
            # 接口请求参数的类型、是一个对象类型、前端对应的是json类型
            type=openapi.TYPE_OBJECT,
            # 设置必须传入的参数
            required=['username', 'password','repwd'],
            # body中的参数选项
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING,description="用户名",default="admin"),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description="密码", default="123456"),
                'repwd': openapi.Schema(type=openapi.TYPE_STRING, description="确认密码", default="123456"),
                'nickname': openapi.Schema(type=openapi.TYPE_STRING, description="用戶名",),
                'sex': openapi.Schema(type=openapi.TYPE_NUMBER, description="性别",),
                'age': openapi.Schema(type=openapi.TYPE_NUMBER, description="年龄",),
                'phone': openapi.Schema(type=openapi.TYPE_STRING, description="手机号码",),
                'introduce': openapi.Schema(type=openapi.TYPE_STRING, description="介绍",),
                'signin': openapi.Schema(type=openapi.TYPE_STRING, description="签名",),
                'tag': openapi.Schema(type=openapi.TYPE_STRING, description="标签",),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description="email",),
                'status': openapi.Schema(type=openapi.TYPE_NUMBER, description="用户状态",default=0),
                'picturePath': openapi.Schema(type=openapi.TYPE_STRING, description="用户头像",default=0),
            },
        ),
        # 接口响应的具体内容
        responses={202: 'id not found'},
        # 进行给这个api备注、swagger ui上显示的内容
        operation_summary='注册'
    )

    def create(self, request, *args,**kwargs):
        # 添加用户
        user_data = request.data
        user_json = CreateUserSerializerModels(data=user_data)  # 必须明确data
        if user_json.is_valid():  # 校验

            if User.objects.filter(username=user_data["username"]):
                return Response(
                    ResponseContent(code=0, message="用户已存在").__dict__
                )

            else:
                user_json.save()  # 保存
                return Response(
                    ResponseContent(code=0, message="注册成功").__dict__
                )

        try:
            return Response(
                ResponseContent(code=1, message=user_json.errors["msg"][0]).__dict__
            )
        except:
            return Response(
                ResponseContent(code=1, message=user_json.errors).__dict__
            )

    token = openapi.Parameter("token", openapi.IN_HEADER, description="token",
                              type=openapi.TYPE_STRING, required=True, )

    @swagger_auto_schema(
        operation_description="获取我的用户信息",
        manual_parameters=[token],
        # 配置接口的请求body、post请求数据是保存在body中的
        # 接口响应的具体内容
        responses={202: 'id not found'},
        # 进行给这个api备注、swagger ui上显示的内容
        operation_summary='获取我的用户信息'
    )
    def retrieve(self,request, *args,**kwargs):
        serializer_class = CreateUserSerializerModels(User.objects.filter(id=kwargs["pk"]).first())
        return Response(serializer_class.data)

class MyAccountCenterViewSet(ViewSet):

    """
    账号中心
    """
    # swagger 分类标签
    swagger_tags = ["账号中心"]
    # 渲染器
    renderer_classes = [JSONRenderer]
    # 权限控制器
    permission_classes = [IsAuthenticated]
    # 认证器
    authentication_classes = [JWTUserToken]
    # 版本控制器
    versioning_class = URLPathVersioning


    @swagger_auto_schema(
        operation_description="获取我的个人信息",
        # 配置接口的请求body、post请求数据是保存在body中的
        request_body=openapi.Schema(
            # 接口请求参数的类型、是一个对象类型、前端对应的是json类型
            type=openapi.TYPE_OBJECT,
            # 设置必须传入的参数
            required=['username', 'password','repwd'],
            # body中的参数选项
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING,description="用户名",default="admin"),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description="密码", default="123456"),
                'repwd': openapi.Schema(type=openapi.TYPE_STRING, description="确认密码", default="123456"),
                'nickname': openapi.Schema(type=openapi.TYPE_STRING, description="用戶名",),
                'sex': openapi.Schema(type=openapi.TYPE_NUMBER, description="性别",),
                'age': openapi.Schema(type=openapi.TYPE_NUMBER, description="年龄",),
                'phone': openapi.Schema(type=openapi.TYPE_STRING, description="手机号码",),
                'introduce': openapi.Schema(type=openapi.TYPE_STRING, description="介绍",),
                'signin': openapi.Schema(type=openapi.TYPE_STRING, description="签名",),
                'tag': openapi.Schema(type=openapi.TYPE_STRING, description="标签",),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description="email",),
                'status': openapi.Schema(type=openapi.TYPE_NUMBER, description="用户状态",default=0),
                'picturePath': openapi.Schema(type=openapi.TYPE_STRING, description="用户头像",default=0),
            },
        ),
        # 接口响应的具体内容
        responses={202: 'id not found'},
        # 进行给这个api备注、swagger ui上显示的内容
        operation_summary='注册'
    )

    def create(self, request, *args,**kwargs):
        # 添加用户
        user_data = request.data
        user_json = CreateUserSerializerModels(data=user_data)  # 必须明确data
        if user_json.is_valid():  # 校验

            if User.objects.filter(username=user_data["username"]):
                return Response(
                    ResponseContent(code=0, message="用户已存在").__dict__
                )

            else:
                user_json.save()  # 保存
                return Response(
                    ResponseContent(code=0, message="注册成功").__dict__
                )
        try:
            return Response(
                ResponseContent(code=1, message=user_json.errors["msg"][0]).__dict__
            )
        except:
            return Response(
                ResponseContent(code=1, message=user_json.errors).__dict__
            )

    token = openapi.Parameter("token", openapi.IN_HEADER, description="token",
                              type=openapi.TYPE_STRING, required=True, )

    @swagger_auto_schema(
        operation_description="获取我的用户信息",
        manual_parameters=[token],
        # 配置接口的请求body、post请求数据是保存在body中的
        # 接口响应的具体内容
        responses={202: 'id not found'},
        # 进行给这个api备注、swagger ui上显示的内容
        operation_summary='获取我的用户信息'
    )
    def list(self,request, *args,**kwargs):
        if request.version == 'v1':
            serializer_class = UserInfoSerializerModels(User.objects.filter(id=request.user).first())
            return Response(ResponseContent(code=0, data=serializer_class.data,message='').__dict__)
        else:
            return Response(ResponseContent(code=1, message="接口版本不正确").__dict__)

# 查询手机号/用户名是否已注册
class AccountCentersViewSet(ViewSet):

    """
    账号中心
    """
    # swagger 分类标签
    swagger_tags = ["账号中心"]
    # 渲染器
    renderer_classes = [JSONRenderer]
    # 版本控制器
    versioning_class = URLPathVersioning

    @swagger_auto_schema(
        operation_description="查询手机号/用户名是否已注册",
        manual_parameters=[
                           openapi.Parameter("username", openapi.IN_QUERY, description="手机号/用户名",
                                             type=openapi.TYPE_STRING, required=True, )
                           ],
        # 配置接口的请求body、post请求数据是保存在body中的
        # 接口响应的具体内容
        responses={202: 'id not found'},
        # 进行给这个api备注、swagger ui上显示的内容
        operation_summary='查询手机号/用户名是否已注册'
    )
    def list(self,request, *args,**kwargs):
        if request.version == 'v1':
            request_data = request.query_params
            if User.objects.filter(username=request_data["username"]):
                return Response(ResponseContent(code=1,message='用户名已存在').__dict__)

            elif User.objects.filter(phone=request_data["username"]):
                return Response(ResponseContent(code=1, message='手机号已注册').__dict__)
            else:
                return Response(ResponseContent(code=0, data=[], message='').__dict__)
        else:
            return Response(ResponseContent(code=1, message="接口版本不正确").__dict__)

class AccountCenterEmailBindViewSet(ViewSet):

    """
    邮箱绑定
    """
    # swagger 分类标签
    swagger_tags = ["账号中心"]
    # 渲染器
    renderer_classes = [JSONRenderer]
    # 版本控制器
    versioning_class = URLPathVersioning

    @swagger_auto_schema(
        operation_description="邮箱绑定",
        manual_parameters=[
                           openapi.Parameter("username", openapi.IN_QUERY, description="手机号/用户名",
                                             type=openapi.TYPE_STRING, required=True, )
                           ],
        # 配置接口的请求body、post请求数据是保存在body中的
        # 接口响应的具体内容
        responses={202: 'id not found'},
        # 进行给这个api备注、swagger ui上显示的内容
        operation_summary='查询手机号/用户名是否已注册'
    )
    def list(self,request, *args,**kwargs):
        if request.version == 'v1':
            request_data = request.query_params
            if User.objects.filter(username=request_data["username"]):
                return Response(ResponseContent(code=1,message='用户名已存在').__dict__)

            elif User.objects.filter(phone=request_data["username"]):
                return Response(ResponseContent(code=1, message='手机号已注册').__dict__)
            else:
                return Response(ResponseContent(code=0, data=[], message='').__dict__)
        else:
            return Response(ResponseContent(code=1, message="接口版本不正确").__dict__)





class testCentersViewSet(ViewSet):

    """
    账号中心
    """
    # swagger 分类标签
    swagger_tags = ["账号中心"]
    # 渲染器
    renderer_classes = [JSONRenderer]
    # 版本控制器
    versioning_class = URLPathVersioning

    @swagger_auto_schema(
        operation_description="查询手机号/用户名是否已注册",
        manual_parameters=[
                           openapi.Parameter("username", openapi.IN_QUERY, description="手机号/用户名",
                                             type=openapi.TYPE_STRING, required=True, )
                           ],
        # 配置接口的请求body、post请求数据是保存在body中的
        # 接口响应的具体内容
        responses={202: 'id not found'},
        # 进行给这个api备注、swagger ui上显示的内容
        operation_summary='查询手机号/用户名是否已注册'
    )
    def list(self,request, *args,**kwargs):
        if request.version == 'v1':
            data = testSerializerModels(Filesave.objects.all(),many=True)
            return Response(ResponseContent(code=1, data=data.data,message="接口版本不正确").__dict__)
        else:
            return Response(ResponseContent(code=1, message="接口版本不正确").__dict__)



# class UserRegisterViewSet(ViewSet):
#
#     """
#     注册
#     """
#     # swagger 分类标签
#     swagger_tags = ["注册"]
#     # 渲染器
#     renderer_classes = [JSONRenderer]
#     # 权限控制器
#     # permission_classes = [IsAuthenticated]
#     # 认证器
#     # authentication_classes = [JWTUserToken]
#     # 版本控制器
#     versioning_class = URLPathVersioning
#
#
#     @swagger_auto_schema(
#         operation_description="注册",
#         # 配置接口的请求body、post请求数据是保存在body中的
#         request_body=openapi.Schema(
#             # 接口请求参数的类型、是一个对象类型、前端对应的是json类型
#             type=openapi.TYPE_OBJECT,
#             # 设置必须传入的参数
#             required=['username', 'password'],
#             # body中的参数选项
#             properties={
#                 'username': openapi.Schema(type=openapi.TYPE_STRING,description="用户名",default="admin"),
#                 'password': openapi.Schema(type=openapi.TYPE_STRING, description="密码", default="123456"),
#                 'repwd': openapi.Schema(type=openapi.TYPE_STRING, description="确认密码", default="123456"),
#                 'nickname': openapi.Schema(type=openapi.TYPE_STRING, description="用戶名",),
#                 'sex': openapi.Schema(type=openapi.TYPE_NUMBER, description="性别",),
#                 'age': openapi.Schema(type=openapi.TYPE_NUMBER, description="年龄",),
#                 'phone': openapi.Schema(type=openapi.TYPE_STRING, description="手机号码",),
#                 'introduce': openapi.Schema(type=openapi.TYPE_STRING, description="介绍",),
#                 'signin': openapi.Schema(type=openapi.TYPE_STRING, description="签名",),
#                 'tag': openapi.Schema(type=openapi.TYPE_STRING, description="标签",),
#                 'email': openapi.Schema(type=openapi.TYPE_STRING, description="email",),
#                 'status': openapi.Schema(type=openapi.TYPE_NUMBER, description="用户状态",default=0),
#                 'picturePath': openapi.Schema(type=openapi.TYPE_STRING, description="用户头像",default=0),
#             },
#         ),
#         # 接口响应的具体内容
#         responses={202: 'id not found'},
#         # 进行给这个api备注、swagger ui上显示的内容
#         operation_summary='注册'
#     )
#
#     def create(self, request, *args,**kwargs):
#         # 添加用户
#         user_data = request.data
#         user_json = CreateUserSerializerModels(data=user_data)  # 必须明确data
#         if user_json.is_valid():  # 校验
#
#             if User.objects.filter(username=user_data["username"]):
#                 return Response(
#                     ResponseContent(code=0, message="用户已存在").__dict__
#                 )
#
#             else:
#                 user_json.save()  # 保存
#                 return Response(
#                     ResponseContent(code=0, message="注册成功").__dict__
#                 )
#
#         try:
#             return Response(
#                 ResponseContent(code=1, message=user_json.errors["msg"][0]).__dict__
#             )
#         except:
#             return Response(
#                 ResponseContent(code=1, message=user_json.errors).__dict__
#             )
#
#
#     token = openapi.Parameter("token", openapi.IN_HEADER, description="token",
#                               type=openapi.TYPE_STRING, required=True, )
#
#     @swagger_auto_schema(
#         operation_description="获取用户列表",
#         manual_parameters=[token],
#         # 配置接口的请求body、post请求数据是保存在body中的
#         # 接口响应的具体内容
#         responses={202: 'id not found'},
#         # 进行给这个api备注、swagger ui上显示的内容
#         operation_summary='获取用户列表'
#     )
#     def list(self, request, *args,**kwargs):
#         if request.version == 'v1':
#             # 处理版本v1的业务逻辑
#             # 返回所有数据集
#             request_serializer = CreateUserSerializerModels(User.objects.all(), many=True)
#
#             context = ResponseContent(code=0, data=request_serializer.data, message="数据获取成功").__dict__
#             return Response(context)
#         else:
#             return Response(ResponseContent(code=1, message="接口版本不正确").__dict__)
#
#     @swagger_auto_schema(
#         operation_description="修改用户信息",
#         manual_parameters=[token],
#         # 配置接口的请求body、post请求数据是保存在body中的
#         request_body=openapi.Schema(
#             # 接口请求参数的类型、是一个对象类型、前端对应的是json类型
#             type=openapi.TYPE_OBJECT,
#             # 设置必须传入的参数
#             required=[],
#             # body中的参数选项
#             properties={
#                 'username': openapi.Schema(type=openapi.TYPE_STRING, description="用户名", default="admin"),
#                 'password': openapi.Schema(type=openapi.TYPE_STRING, description="密码", default="123456"),
#                 'nickname': openapi.Schema(type=openapi.TYPE_STRING, description="用戶名", ),
#                 'sex': openapi.Schema(type=openapi.TYPE_NUMBER, description="性别", ),
#                 'age': openapi.Schema(type=openapi.TYPE_NUMBER, description="年龄", ),
#                 'phone': openapi.Schema(type=openapi.TYPE_STRING, description="手机号码", ),
#                 'introduce': openapi.Schema(type=openapi.TYPE_STRING, description="介绍", ),
#                 'signin': openapi.Schema(type=openapi.TYPE_STRING, description="签名", ),
#                 'tag': openapi.Schema(type=openapi.TYPE_STRING, description="标签", ),
#                 'email': openapi.Schema(type=openapi.TYPE_STRING, description="email", ),
#                 'status': openapi.Schema(type=openapi.TYPE_NUMBER, description="用户状态", default=0),
#                 'picturePath': openapi.Schema(type=openapi.TYPE_STRING, description="用户头像", default=0),
#             },
#         ),
#         # 接口响应的具体内容
#         responses={202: 'id not found'},
#         # 进行给这个api备注、swagger ui上显示的内容
#         operation_summary='修改用户信息'
#     )
#     def partial_update(self,request, *args,**kwargs):
#         if request.version == 'v1':
#             user_data = request.data
#             try:
#                 user_json = CreateUserSerializerModels(instance=User.objects.get(id=user_data["id"]),data=user_data)
#                 if user_json.is_valid():
#                     user_json.save()
#                     return Response(ResponseContent(code=0, message="用户修改成功").__dict__)
#             except:
#                 return Response(ResponseContent(code=1, message="该用户不存在").__dict__)
#
#             return Response(ResponseContent(code=0, message=user_json.errors).__dict__)
#
#         else:
#             return Response(ResponseContent(code=1, message="接口版本不正确").__dict__)
#
#     token = openapi.Parameter("token", openapi.IN_HEADER, description="token",
#                               type=openapi.TYPE_STRING, required=True, )
#
#     @swagger_auto_schema(
#         operation_description="获取指定用户详情",
#         manual_parameters=[token],
#         # 配置接口的请求body、post请求数据是保存在body中的
#         # 接口响应的具体内容
#         responses={202: 'id not found'},
#         # 进行给这个api备注、swagger ui上显示的内容
#         operation_summary='获取指定用户详情'
#     )
#     def retrieve(self,request, *args,**kwargs):
#         serializer_class = CreateUserSerializerModels(User.objects.filter(id=kwargs["pk"]).first())
#         return Response(serializer_class.data)
#
#
#     @swagger_auto_schema(
#         operation_description="删除指定用户",
#         manual_parameters=[token],
#         # 配置接口的请求body、post请求数据是保存在body中的
#         # 接口响应的具体内容
#         responses={202: 'id not found'},
#         # 进行给这个api备注、swagger ui上显示的内容
#         operation_summary='删除指定用户'
#     )
#     def destroy(self,request, *args,**kwargs):
#         """
#         删除指定用户
#         """
#
#         if request.version == 'v1':
#             if User.objects.filter(id=kwargs["pk"]):
#                 User.objects.filter(id=kwargs["pk"]).delete()
#                 return Response(ResponseContent(code=0, message="数据删除成功").__dict__)
#             else:
#                 return Response(ResponseContent(code=1, message="数据不存在").__dict__)
#
#         return Response(ResponseContent(code=1, message="接口版本不正确").__dict__)



class UserAccounStatustViewSet(ViewSet):

    """
    用户禁用与解禁
    0 禁用 1 正常
    """
    # swagger 分类标签
    swagger_tags = ["用户管理"]
    # 渲染器
    renderer_classes = [JSONRenderer]
    # 权限控制器
    permission_classes = [IsAuthenticated]
    # 认证器
    authentication_classes = [JWTUserToken]
    # 版本控制器
    versioning_class = URLPathVersioning

    token = openapi.Parameter("token", openapi.IN_HEADER, description="token",
                              type=openapi.TYPE_STRING, required=True, )

    @swagger_auto_schema(
        # operation_description="禁用用户",
        manual_parameters=[token],
        # 配置接口的请求body、post请求数据是保存在body中的
        request_body=openapi.Schema(
            # 接口请求参数的类型、是一个对象类型、前端对应的是json类型
            type=openapi.TYPE_OBJECT,
            # 设置必须传入的参数
            required=['status'],
            # body中的参数选项
            properties={
                'status': openapi.Schema(type=openapi.TYPE_STRING, description="状态", ),
            },
        ),
        # 接口响应的具体内容
        responses={202: 'id not found'},
        # 进行给这个api备注、swagger ui上显示的内容
        operation_summary='禁用用户'
    )
    def partial_update(self,request, *args,**kwargs):
        """
        用户禁用与解禁
        0 禁用 1 正常
        """
        if request.version == 'v1':
            try:
                User.objects.filter(id=kwargs["pk"]).update(status=request.data["status"])
                return Response(ResponseContent(code=0, message="操作成功").__dict__)
            except:
                return Response(ResponseContent(code=1, message="该用户不存在").__dict__)

        else:
            return Response(ResponseContent(code=1, message="接口版本不正确").__dict__)



class UserAccounBatchUpdateStatustView(ViewSet):

    """
    批量用户禁用与解禁
    0 禁用 1 正常
    """
    # swagger 分类标签
    swagger_tags = ["用户管理"]
    # 渲染器
    renderer_classes = [JSONRenderer]
    # 权限控制器
    permission_classes = [IsAuthenticated]
    # 认证器
    authentication_classes = [JWTUserToken]
    # 版本控制器
    versioning_class = URLPathVersioning

    token = openapi.Parameter("token", openapi.IN_HEADER, description="token",
                              type=openapi.TYPE_STRING, required=True, )
    @swagger_auto_schema(
        # operation_description="获取指定用户详情",
        manual_parameters=[token],
        # 配置接口的请求body、post请求数据是保存在body中的
        request_body=openapi.Schema(
            # 接口请求参数的类型、是一个对象类型、前端对应的是json类型
            type=openapi.TYPE_OBJECT,
            # 设置必须传入的参数
            required=['status'],
            # body中的参数选项
            properties={
                'id': openapi.Schema(type=openapi.TYPE_ARRAY, description="用户id", items=openapi.TYPE_ARRAY),
                'status': openapi.Schema(type=openapi.TYPE_STRING, description="状态", ),
            },
        ),
        # 接口响应的具体内容
        responses={202: 'id not found'},
        # 进行给这个api备注、swagger ui上显示的内容
        operation_summary='批量用户禁用与解禁'
    )
    def update(self,request, *args,**kwargs):
        """
        批量用户禁用与解禁
        0 禁用 1 正常
        """
        data = request.data
        if request.version == 'v1':
            try:
                data = [User.objects.filter(id=x).update(status=data["status"]) for x in data["id"]]
                return Response(ResponseContent(code=0, message="操作成功").__dict__)
            except:
                return Response(ResponseContent(code=1, message="该用户不存在").__dict__)

        else:
            return Response(ResponseContent(code=1, message="接口版本不正确").__dict__)



class UserBatchDeleteView(ViewSet):

    """
    批量删除用户
    """
    # swagger 分类标签
    swagger_tags = ["用户管理"]
    # 渲染器
    renderer_classes = [JSONRenderer]
    # 权限控制器
    permission_classes = [IsAuthenticated]
    # 认证器
    authentication_classes = [JWTUserToken]
    # 版本控制器
    versioning_class = URLPathVersioning




    token = openapi.Parameter("token", openapi.IN_HEADER, description="token",
                              type=openapi.TYPE_STRING, required=True, )
    @swagger_auto_schema(
        # operation_description="获取指定用户详情",
        manual_parameters=[token],
        # 配置接口的请求body、post请求数据是保存在body中的
        request_body=openapi.Schema(
            # 接口请求参数的类型、是一个对象类型、前端对应的是json类型
            type=openapi.TYPE_OBJECT,
            # 设置必须传入的参数
            required=['status'],
            # body中的参数选项
            properties={
                'id': openapi.Schema(type=openapi.TYPE_ARRAY, description="用户id", items=openapi.TYPE_ARRAY),
            },
        ),
        # 接口响应的具体内容
        responses={202: 'id not found'},
        # 进行给这个api备注、swagger ui上显示的内容
        operation_summary='批量删除用户'
    )
    def delete(self,request, *args,**kwargs):
        """
        批量删除用户
        """

        if request.version == 'v1':
            try:
                data = request.data
                status = [User.objects.filter(id=x).update(isDelete=1) for x in data["id"]]
                return Response(ResponseContent(code=0, message="操作成功").__dict__)
            except:
                return Response(ResponseContent(code=1, message="该用户不存在").__dict__)

        else:
            return Response(ResponseContent(code=1, message="接口版本不正确").__dict__)




class MyTokenRefreshView(TokenViewBase):
    """
    自定义刷新token refresh: 刷新token的元素
    """

    def get_serializer_class(self):
        """不同的版本使用不同的序列化类"""
        if self.request.version == 'v1':
            serializer_class = TokenRefreshSerializer
            return
        else:
            return


