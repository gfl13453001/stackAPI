import time

from django.shortcuts import render

# Create your views here.
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning
from rest_framework.viewsets import ViewSet

from apps.article.models import Classify, Article
from common.authenticationclass import JWTUserToken
from common.main import ResponseContent
from common.serializerset.articles import ClassifySerializerModels, ArticleSerializerModels, \
    ArticleSerializerDetailModels, ArticleListSerializerModels, ArticleSerializerEditModels


# from common.serializerset.system import NavSerializerModels


class  ArticleClassifyViewSet(ViewSet):

    """
    文章模块
    """
    # swagger 分类标签
    swagger_tags = ["文章模块"]
    # 渲染器
    renderer_classes = [JSONRenderer]
    # 版本控制器
    versioning_class = URLPathVersioning

    @swagger_auto_schema(
        operation_description="获取分类列表",
        manual_parameters=[],
        # 配置接口的请求body、post请求数据是保存在body中的
        # 接口响应的具体内容
        responses={202: 'id not found'},
        # 进行给这个api备注、swagger ui上显示的内容
        operation_summary='获取分类列表'
    )
    def list(self, request, *args,**kwargs):

        if request.version == 'v1':
            # 处理版本v1的业务逻辑
            # 返回所有数据集
            serializer  = ClassifySerializerModels(Classify.objects.filter(isDelete=0,isShow=1), many=True)

            context = ResponseContent(code=0, data=serializer .data, message="数据获取成功").__dict__
            return Response(context)
        else:
            return Response(ResponseContent(code=1, message="接口版本不正确").__dict__)


    @swagger_auto_schema(
        operation_description="获取分类详情",
        manual_parameters=[],
        # 配置接口的请求body、post请求数据是保存在body中的
        # 接口响应的具体内容
        responses={202: 'id not found'},
        # 进行给这个api备注、swagger ui上显示的内容
        operation_summary='获取分类详情'
    )
    def retrieve(self,request, *args,**kwargs):
        if request.version == 'v1':
            # 处理版本v1的业务逻辑
            # 返回所有数据集
            serializer_class = ClassifySerializerModels(Classify.objects.filter(id=kwargs["pk"],isDelete=0).first())

            context = ResponseContent(code=0, data=serializer_class.data, message="数据获取成功").__dict__
            return Response(context)
        else:
            return Response(ResponseContent(code=1, message="接口版本不正确").__dict__)


class CreateArticleViewSet(ViewSet):

    """
    文章模块
    """
    # swagger 分类标签
    swagger_tags = ["文章模块"]
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
        operation_description="发布文章",
        manual_parameters=[token],
        # 配置接口的请求body、post请求数据是保存在body中的
        request_body=openapi.Schema(
            # 接口请求参数的类型、是一个对象类型、前端对应的是json类型
            type=openapi.TYPE_OBJECT,
            # 设置必须传入的参数
            required=['name',],
            # body中的参数选项
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING,description="文章标题",default="首页"),
                'content': openapi.Schema(type=openapi.TYPE_STRING, description="内容",),
                'description': openapi.Schema(type=openapi.TYPE_STRING, description="描述",),
                'sort': openapi.Schema(type=openapi.TYPE_NUMBER, description="排序",),
                'type': openapi.Schema(type=openapi.TYPE_NUMBER, description="分类类型",default=0),
                'isShow': openapi.Schema(type=openapi.TYPE_NUMBER, description="是否显示",),
                'img': openapi.Schema(type=openapi.TYPE_STRING, description="封面id",),
                'classify': openapi.Schema(type=openapi.TYPE_STRING, description="分类id",),
            },
        ),
        # 接口响应的具体内容
        responses={202: 'id not found'},
        operation_summary='发布文章'
    )

    def create(self, request, *args,**kwargs):
        # 发布文章
        request.data["userid"] = request.user.id
        request_data = request.data
        article_json = ArticleSerializerModels(data=request_data)
        if article_json.is_valid():  # 校验
            data = article_json.save()
            if data == 1:
                return Response(
                    ResponseContent(code=1, message="作者id、分类id或者封面id不存在、无法发布文章",messageCode=40001).__dict__
                )
            else:
                return Response(
                    ResponseContent(code=0, message="文章发布成功",messageCode=20001).__dict__
                )
        else:
            return Response(
                ResponseContent(code=0, message=article_json.errors,messageCode=40002).__dict__
            )


    token = openapi.Parameter("token", openapi.IN_HEADER, description="token",
                              type=openapi.TYPE_STRING, required=True, )

    @swagger_auto_schema(
        operation_description="编辑文章",
        manual_parameters=[token],
        # 配置接口的请求body、post请求数据是保存在body中的
        request_body=openapi.Schema(
            # 接口请求参数的类型、是一个对象类型、前端对应的是json类型
            type=openapi.TYPE_OBJECT,
            # 设置必须传入的参数
            required=[],
            # body中的参数选项
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING,description="文章标题",default="首页"),
                'content': openapi.Schema(type=openapi.TYPE_STRING, description="内容",),
                'description': openapi.Schema(type=openapi.TYPE_STRING, description="描述",),
                'sort': openapi.Schema(type=openapi.TYPE_NUMBER, description="排序",),
                'type': openapi.Schema(type=openapi.TYPE_NUMBER, description="分类类型",default=0),
                'isShow': openapi.Schema(type=openapi.TYPE_NUMBER, description="是否显示",),
                'img': openapi.Schema(type=openapi.TYPE_STRING, description="封面id",),
                'classify': openapi.Schema(type=openapi.TYPE_STRING, description="分类id",),
            },
        ),
        # 接口响应的具体内容
        responses={202: 'id not found'},
        # 进行给这个api备注、swagger ui上显示的内容
        operation_summary='编辑文章'
    )
    def update(self,request, *args,**kwargs):
        """
        """
        if request.version == 'v1':
            article_data = request.data
            try:
                article_json = ArticleSerializerEditModels(Article.objects.get(id=kwargs["pk"]),data=article_data)
                if article_json.is_valid():
                    data = article_json.save()

                    if data == 1:
                        return Response(ResponseContent(code=1, message="修改异常",messageCode=40002).__dict__)

                    return Response(ResponseContent(code=0, message="修改成功",messageCode=20001).__dict__)
                else:
                    return Response(ResponseContent(code=0, message=article_json.errors,messageCode=40004).__dict__)
            except:
                return Response(ResponseContent(code=1, message="该数据不存在",messageCode=40004).__dict__)
        else:
            return Response(ResponseContent(code=1, message="接口版本不正确",messageCode=40005).__dict__)

    token = openapi.Parameter("token", openapi.IN_HEADER, description="token",
                              type=openapi.TYPE_STRING, required=True, )


    @swagger_auto_schema(
        operation_description="删除文章",
        manual_parameters=[token],
        # 配置接口的请求body、post请求数据是保存在body中的
        # 接口响应的具体内容
        responses={202: 'id not found'},
        # 进行给这个api备注、swagger ui上显示的内容
        operation_summary='删除文章'
    )
    def destroy(self,request, *args,**kwargs):
        """
        删除文章
        """

        if request.version == 'v1':
            if Article.objects.filter(id=kwargs["pk"]):
                Article.objects.filter(id=kwargs["pk"]).update(isDelete=1,deleteTime=int(time.time()))
                return Response(ResponseContent(code=0, message="数据删除成功").__dict__)
            else:
                return Response(ResponseContent(code=1, message="数据不存在").__dict__)

        return Response(ResponseContent(code=1, message="接口版本不正确").__dict__)
    token = openapi.Parameter("token", openapi.IN_HEADER, description="token",
                              type=openapi.TYPE_STRING, required=True, )


    @swagger_auto_schema(
        operation_description="查询文章详情",
        manual_parameters=[token],
        # 配置接口的请求body、post请求数据是保存在body中的
        # 接口响应的具体内容
        responses={202: 'id not found'},
        # 进行给这个api备注、swagger ui上显示的内容
        operation_summary='查询文章详情'
    )
    def retrieve(self,request, *args,**kwargs):
        """
        查询文章详情
        """

        if request.version == 'v1':
            if Article.objects.filter(id=kwargs["pk"]):

                get_data = ArticleListSerializerModels(Article.objects.filter(id=kwargs["pk"],isDelete=0).first())
                return Response(ResponseContent(code=0, message="查询成功",data=get_data.data).__dict__)
            else:
                return Response(ResponseContent(code=1, message="数据不存在").__dict__)

        return Response(ResponseContent(code=1, message="接口版本不正确").__dict__)


class GetArticleViewSet(ViewSet):

    """
    文章模块
    """
    # swagger 分类标签
    swagger_tags = ["文章模块"]
    # 渲染器
    renderer_classes = [JSONRenderer]
    # 版本控制器
    versioning_class = URLPathVersioning

    @swagger_auto_schema(
        operation_description="获取文章列表",
        manual_parameters=[],
        # 配置接口的请求body、post请求数据是保存在body中的
        # 接口响应的具体内容
        responses={202: 'id not found'},
        # 进行给这个api备注、swagger ui上显示的内容
        operation_summary='获取文章列表'
    )
    def list(self, request, *args,**kwargs):
        if request.version == 'v1':
            # 处理版本v1的业务逻辑
            # 返回所有数据集
            serializer  = ArticleSerializerModels(Article.objects.filter(isDelete=0), many=True)

            context = ResponseContent(code=0, data=serializer .data, message="数据获取成功").__dict__
            return Response(context)
        else:
            return Response(ResponseContent(code=1, message="接口版本不正确").__dict__)


    @swagger_auto_schema(
        operation_description="获取文章详情",
        manual_parameters=[],
        # 配置接口的请求body、post请求数据是保存在body中的
        # 接口响应的具体内容
        responses={202: 'id not found'},
        # 进行给这个api备注、swagger ui上显示的内容
        operation_summary='获取文章详情'
    )
    def retrieve(self,request, *args,**kwargs):
        print(kwargs["pk"])
        serializer_class = ArticleListSerializerModels(Article.objects.filter(id=kwargs["pk"],isDelete=0).first(),many=True)
        return Response(serializer_class.data)


class ClassifyGetArticleViewSet(ViewSet):

    """
    文章模块
    """
    # swagger 分类标签
    swagger_tags = ["文章模块"]
    # 渲染器
    renderer_classes = [JSONRenderer]
    # 版本控制器
    versioning_class = URLPathVersioning

    @swagger_auto_schema(
        operation_description="查询指定分类下文章",
        manual_parameters=[openapi.Parameter("id", openapi.IN_QUERY, description="分类id",
                              type=openapi.TYPE_STRING, required=True, )],
        # 配置接口的请求body、post请求数据是保存在body中的
        # 接口响应的具体内容
        responses={202: 'id not found'},
        # 进行给这个api备注、swagger ui上显示的内容
        operation_summary='查询指定分类下文章'
    )
    def list(self, request, *args,**kwargs):
        request_data = request.query_params
        if request.version == 'v1':
            # 处理版本v1的业务逻辑
            # 返回所有数据集
            serializer  = ArticleListSerializerModels(Article.objects.filter(isDelete=0,isShow=1,classify_id=request_data["id"]), many=True)

            context = ResponseContent(code=0, data=serializer .data, message="数据获取成功").__dict__
            return Response(context)
        else:
            return Response(ResponseContent(code=1, message="接口版本不正确").__dict__)


    @swagger_auto_schema(
        operation_description="获取文章详情",
        manual_parameters=[],
        # 配置接口的请求body、post请求数据是保存在body中的
        # 接口响应的具体内容
        responses={202: 'id not found'},
        # 进行给这个api备注、swagger ui上显示的内容
        operation_summary='获取文章详情'
    )
    def retrieve(self,request, *args,**kwargs):
        print(1)
        serializer_class = ArticleSerializerModels(Article.objects.filter(id=kwargs["pk"],isDelete=0).first())
        return Response(serializer_class.data)



class MyArticleViewSet(ViewSet):

    """
    文章模块
    """
    # swagger 分类标签
    swagger_tags = ["文章模块"]
    # 渲染器
    renderer_classes = [JSONRenderer]
    # 版本控制器
    versioning_class = URLPathVersioning


    @swagger_auto_schema(
        operation_description="获取指定用户文章列表",
        manual_parameters=[openapi.Parameter("userid", openapi.IN_QUERY, description="userid",
                              type=openapi.TYPE_STRING, required=True, )],
        # 配置接口的请求body、post请求数据是保存在body中的
        # 接口响应的具体内容
        responses={202: 'id not found'},
        # 进行给这个api备注、swagger ui上显示的内容
        operation_summary='获取指定用户文章列表'
    )
    def list(self, request, *args,**kwargs):

        request_data = request.query_params
        if request.version == 'v1':
            # 处理版本v1的业务逻辑
            # 返回所有数据集
            serializer  = ArticleListSerializerModels(Article.objects.filter(user_id=request_data["userid"],isDelete=0,isShow=1), many=True)

            context = ResponseContent(code=0, data=serializer .data, message="数据获取成功").__dict__
            return Response(context)
        else:
            return Response(ResponseContent(code=1, message="接口版本不正确").__dict__)
