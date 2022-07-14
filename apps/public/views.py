import os

from django.http import QueryDict
from django.shortcuts import render

# Create your views here.
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning
from rest_framework.viewsets import ViewSet

from apps.public.models import Nav, Banner
from apps.user.models import Filesave
from common.libs.qianniu import upload
from common.main import ResponseContent, getID
from common.serializerset.public import NavSerializerModels, BannerSerializerModels, UploadFIleSerializerModels
from stackNoteAPI.settings.dev import OSS_FILEPATH


class MenuNavigationViewSet(ViewSet):

    """
    菜单导航
    """
    # swagger 分类标签
    swagger_tags = ["菜单导航"]
    # 渲染器
    renderer_classes = [JSONRenderer]

    # 版本控制器
    versioning_class = URLPathVersioning


    # @swagger_auto_schema(
    #     operation_description="获取我的个人信息",
    #     # 配置接口的请求body、post请求数据是保存在body中的
    #     request_body=openapi.Schema(
    #         # 接口请求参数的类型、是一个对象类型、前端对应的是json类型
    #         type=openapi.TYPE_OBJECT,
    #         # 设置必须传入的参数
    #         required=['username', 'password','repwd'],
    #         # body中的参数选项
    #         properties={
    #             'username': openapi.Schema(type=openapi.TYPE_STRING,description="用户名",default="admin"),
    #             'password': openapi.Schema(type=openapi.TYPE_STRING, description="密码", default="123456"),
    #             'repwd': openapi.Schema(type=openapi.TYPE_STRING, description="确认密码", default="123456"),
    #             'nickname': openapi.Schema(type=openapi.TYPE_STRING, description="用戶名",),
    #             'sex': openapi.Schema(type=openapi.TYPE_NUMBER, description="性别",),
    #             'age': openapi.Schema(type=openapi.TYPE_NUMBER, description="年龄",),
    #             'phone': openapi.Schema(type=openapi.TYPE_STRING, description="手机号码",),
    #             'introduce': openapi.Schema(type=openapi.TYPE_STRING, description="介绍",),
    #             'signin': openapi.Schema(type=openapi.TYPE_STRING, description="签名",),
    #             'tag': openapi.Schema(type=openapi.TYPE_STRING, description="标签",),
    #             'email': openapi.Schema(type=openapi.TYPE_STRING, description="email",),
    #             'status': openapi.Schema(type=openapi.TYPE_NUMBER, description="用户状态",default=0),
    #             'picturePath': openapi.Schema(type=openapi.TYPE_STRING, description="用户头像",default=0),
    #         },
    #     ),
    #     # 接口响应的具体内容
    #     responses={202: 'id not found'},
    #     # 进行给这个api备注、swagger ui上显示的内容
    #     operation_summary='注册'
    # )

    # def create(self, request, *args,**kwargs):
    #     # 添加用户
    #     user_data = request.data
    #     user_json = CreateUserSerializerModels(data=user_data)  # 必须明确data
    #     if user_json.is_valid():  # 校验
    #
    #         if User.objects.filter(username=user_data["username"]):
    #             return Response(
    #                 ResponseContent(code=0, message="用户已存在").__dict__
    #             )
    #
    #         else:
    #             user_json.save()  # 保存
    #             return Response(
    #                 ResponseContent(code=0, message="注册成功").__dict__
    #             )
    #
    #     try:
    #         return Response(
    #             ResponseContent(code=1, message=user_json.errors["msg"][0]).__dict__
    #         )
    #     except:
    #         return Response(
    #             ResponseContent(code=1, message=user_json.errors).__dict__
    #         )

    @swagger_auto_schema(
        operation_description="获取菜单导航",
        manual_parameters=[],
        # 配置接口的请求body、post请求数据是保存在body中的
        # 接口响应的具体内容
        responses={202: 'id not found'},
        # 进行给这个api备注、swagger ui上显示的内容
        operation_summary='获取菜单导航'
    )
    def list(self,request, *args,**kwargs):
        serializer_class = NavSerializerModels(Nav.objects.filter(isDelete=0,isShow=1),many=True)
        return Response(
            ResponseContent(code=0, data= serializer_class.data,message="").__dict__

           )

class BannerViewSet(ViewSet):

    """
    首页banner
    """
    # swagger 分类标签
    swagger_tags = ["首页"]
    # 渲染器
    renderer_classes = [JSONRenderer]

    # 版本控制器
    versioning_class = URLPathVersioning


    @swagger_auto_schema(
        operation_description="获取banner列表",
        manual_parameters=[],
        # 配置接口的请求body、post请求数据是保存在body中的
        # 接口响应的具体内容
        responses={202: 'id not found'},
        # 进行给这个api备注、swagger ui上显示的内容
        operation_summary='获取banner列表'
    )
    def list(self,request, *args,**kwargs):
        serializer_class = BannerSerializerModels(Banner.objects.filter(isDelete=0,isShow=1),many=True)
        return Response(
            ResponseContent(code=0, data= serializer_class.data,message="").__dict__

           )






class UploadFileView(ViewSet):

    """
    文件上传
    """
    # swagger 分类标签
    swagger_tags = ["文件上传"]
    # 渲染器
    renderer_classes = [JSONRenderer]
    # 权限控制器
    # permission_classes = [IsAuthenticated]
    # 认证器
    # authentication_classes = [JWTUserToken]
    # 版本控制器
    versioning_class = URLPathVersioning

    # 解决swagger 无法处理上传文件的解析器
    parser_classes = (MultiPartParser,)

    # # token
    # token = openapi.Parameter("token", openapi.IN_HEADER, description="token",
    #                           type=openapi.TYPE_STRING, required=True, )
    #


    file = openapi.Parameter("file", in_=openapi.IN_FORM, description="file",
                                  type=openapi.TYPE_FILE,)
    @swagger_auto_schema(
        manual_parameters=[file],
        # 接口响应的具体内容
        responses={202: 'id not found'},
        # 进行给这个api备注、swagger ui上显示的内容
        operation_summary='文件上传'
    )

    def create(self, request, *args,**kwargs):

        file_data = request.data
        print(file_data)

        get_upload_filename = file_data["file"].name

        file_id = getID(index=40)
        save_filename = os.path.join(OSS_FILEPATH,get_upload_filename)
        if request.version == "v1":
            with open(save_filename, "wb") as f:
                for i in file_data["file"].chunks():
                    f.write(i)

            res = upload(filename=get_upload_filename, path=save_filename)
            response_data = f"id={file_id}&fileName={get_upload_filename}&fileType={file_data['file'].content_type}" \
                            f"&url={res.get('file').get('url')}&size={file_data['file'].size}"

            ct = QueryDict(query_string=response_data)

            data_json = UploadFIleSerializerModels(data=ct)

            if data_json.is_valid():

                data_json.save()
                data = {
                    "id":file_id,
                    "file":{
                        "file":get_upload_filename,"type":file_data['file'].content_type,"url":res.get('file').get('url'),
                        "size":file_data['file'].size
                    }
                }
                os.remove(save_filename) if os.path.exists(save_filename) else 1
                return Response(ResponseContent(code=0, data=data,message="上传成功").__dict__)
            else:
                return Response(
                    ResponseContent(code=1, message=data_json.errors).__dict__
                )

        else:
            return Response(ResponseContent(code=1, message="接口版本不正确").__dict__)



    token = openapi.Parameter("token", openapi.IN_HEADER, description="token",
                              type=openapi.TYPE_STRING, required=True, )

    @swagger_auto_schema(
        operation_description="获取文件列表",
        manual_parameters=[token],
        # 配置接口的请求body、post请求数据是保存在body中的
        # 接口响应的具体内容
        responses={202: 'id not found'},
        # 进行给这个api备注、swagger ui上显示的内容
        operation_summary='获取文件列表'
    )
    def list(self, request, *args,**kwargs):
        if request.version == 'v1':
            # 处理版本v1的业务逻辑
            # 返回所有数据集
            request_serializer = UploadFIleSerializerModels(Filesave.objects.all(), many=True)

            context = ResponseContent(code=0, data=request_serializer.data, message="数据获取成功").__dict__
            return Response(context)
        else:
            return Response(ResponseContent(code=1, message="接口版本不正确").__dict__)


    @swagger_auto_schema(
        operation_description="获取文件详细信息",
        manual_parameters=[token],
        # 配置接口的请求body、post请求数据是保存在body中的
        # 接口响应的具体内容
        responses={202: 'id not found'},
        # 进行给这个api备注、swagger ui上显示的内容
        operation_summary='获取文件详细信息'
    )
    def retrieve(self,request, *args,**kwargs):
        if request.version == 'v1':
            # 处理版本v1的业务逻辑
            # 返回所有数据集
            serializer_class = UploadFIleSerializerModels(Filesave.objects.filter(id=kwargs["pk"]).first())

            context = ResponseContent(code=0, data=serializer_class.data, message="数据获取成功").__dict__
            return Response(context)
        else:
            return Response(ResponseContent(code=1, message="接口版本不正确").__dict__)


