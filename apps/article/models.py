from django.db import models


# 文章分类模型
from apps.user.models import Filesave, User


class Classify(models.Model):
    id = models.CharField(primary_key=True, max_length=40, verbose_name='id')
    name = models.CharField( max_length=8, verbose_name='分类名称')
    description = models.CharField(null=True, max_length=40, verbose_name='描述')
    createTime = models.CharField(null=True, max_length=10, verbose_name='创建时间')
    updateTime = models.CharField(null=True, max_length=10, verbose_name='修改时间')
    deleteTime = models.CharField(null=True, max_length=10, verbose_name='删除时间')
    type = models.IntegerField(null=True,default=0,verbose_name='类型')
    # 0为文章分类
    sort = models.IntegerField(verbose_name='排序',default=0)
    isDelete = models.IntegerField(null=True, default=0, verbose_name='删除状态')
    # 0 为不删除、1为删除	逻辑删除标记
    isShow = models.IntegerField(null=True, default=1, verbose_name='显示状态')
    # 0 为不显示、1为显示	显示状态
    create_by = models.CharField(null=True, max_length=20, verbose_name='创建人')


    def __str__(self):
          # 在该模型被关联是默认显示的字段
        return self.id

    class Meta:
        #   自定义表名
        db_table = 'stack_article_classify'
        # 表备注
        verbose_name_plural = "文章分类表"
        verbose_name = verbose_name_plural

class Article(models.Model):
    id = models.CharField(primary_key=True, max_length=10, verbose_name='id')
    title = models.CharField( max_length=20, verbose_name='文章标题')
    description = models.CharField(null=True, max_length=80, verbose_name='描述')
    content = models.TextField(verbose_name='内容')
    createTime = models.DateTimeField(null=True, max_length=10, verbose_name='创建时间')
    updateTime = models.DateTimeField(null=True, max_length=10, verbose_name='修改时间')
    deleteTime = models.DateTimeField(null=True, max_length=10, verbose_name='删除时间')
    type = models.IntegerField(null=True,default=0,verbose_name='类型')
    # 0为文章分类
    # views = models.IntegerField(null=True,default=0,verbose_name='预览数')
    sort = models.IntegerField(null=True,verbose_name='排序',default=0)
    isDelete = models.IntegerField(null=True, default=0, verbose_name='删除状态')
    # 0 为不删除、1为删除	逻辑删除标记
    isShow = models.IntegerField(null=True, default=1, verbose_name='显示状态')
    # 0 为不显示、1为显示	显示状态
    check = models.IntegerField(null=True, default=2, verbose_name='审核状态')
    # 0 为未通过、1为通过	2 审核中
    img = models.ForeignKey(Filesave, null=True, on_delete=models.SET_NULL, verbose_name='文件id')
    user = models.ForeignKey(User,null=True,  on_delete=models.SET_NULL, verbose_name='用户id')
    classify = models.ForeignKey(Classify, null=True, on_delete=models.SET_NULL, verbose_name='分类id')



    def __str__(self):
          # 在该模型被关联是默认显示的字段
        return self.id

    class Meta:
        #   自定义表名
        db_table = 'stack_article'
        # 表备注
        verbose_name_plural = "文章表"
        verbose_name = verbose_name_plural


