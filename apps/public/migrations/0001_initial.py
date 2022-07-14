# Generated by Django 3.2.4 on 2021-09-16 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='id')),
                ('title', models.CharField(max_length=20, verbose_name='标题')),
                ('path', models.CharField(max_length=40, null=True, verbose_name='跳转路径')),
                ('description', models.CharField(max_length=40, null=True, verbose_name='描述')),
                ('createTime', models.CharField(max_length=10, null=True, verbose_name='创建时间')),
                ('updateTime', models.CharField(max_length=10, null=True, verbose_name='修改时间')),
                ('deleteTime', models.CharField(max_length=10, null=True, verbose_name='删除时间')),
                ('sort', models.IntegerField(default=0, verbose_name='排序')),
                ('isDelete', models.IntegerField(default=0, null=True, verbose_name='删除状态')),
                ('isShow', models.IntegerField(default=0, null=True, verbose_name='显示状态')),
                ('create_by', models.CharField(max_length=20, null=True, verbose_name='创建人')),
            ],
            options={
                'verbose_name': 'banner表',
                'verbose_name_plural': 'banner表',
                'db_table': 'stack_index_banner',
            },
        ),
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='id')),
                ('title', models.CharField(max_length=8, verbose_name='标题')),
                ('path', models.CharField(max_length=20, verbose_name='路由路径')),
                ('description', models.CharField(max_length=40, null=True, verbose_name='描述')),
                ('createTime', models.CharField(max_length=10, null=True, verbose_name='创建时间')),
                ('updateTime', models.CharField(max_length=10, null=True, verbose_name='修改时间')),
                ('deleteTime', models.CharField(max_length=10, null=True, verbose_name='删除时间')),
                ('sort', models.IntegerField(default=0, verbose_name='排序')),
                ('isDelete', models.IntegerField(default=0, null=True, verbose_name='删除状态')),
                ('isShow', models.IntegerField(default=0, null=True, verbose_name='显示状态')),
                ('create_by', models.CharField(max_length=20, null=True, verbose_name='创建人')),
            ],
            options={
                'verbose_name': '导航表',
                'verbose_name_plural': '导航表',
                'db_table': 'stack_index_nav',
            },
        ),
    ]