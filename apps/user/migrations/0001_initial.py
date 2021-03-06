# Generated by Django 3.2.4 on 2022-07-19 03:57

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filesave',
            fields=[
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='id')),
                ('fileType', models.CharField(max_length=80, verbose_name='文件类型')),
                ('fileName', models.CharField(max_length=80, verbose_name='名称')),
                ('createTime', models.CharField(max_length=10, verbose_name='时间')),
                ('deleteTime', models.CharField(max_length=10, verbose_name='删除时间')),
                ('isDelete', models.IntegerField(default=1, verbose_name='逻辑删除标记')),
                ('url', models.CharField(max_length=200, verbose_name='在线url')),
                ('size', models.IntegerField(null=True, verbose_name='文件大小')),
            ],
            options={
                'verbose_name_plural': '文件上传',
                'db_table': 'stack_file',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='id')),
                ('nickname', models.CharField(max_length=20, null=True, verbose_name='昵称')),
                ('sex', models.IntegerField(default=0, null=True, verbose_name='性别')),
                ('age', models.IntegerField(default=0, null=True, verbose_name='年龄')),
                ('phone', models.CharField(max_length=11, verbose_name='电话')),
                ('role', models.CharField(default='MEMBER', max_length=10, null=True, verbose_name='用户角色')),
                ('introduce', models.CharField(max_length=80, null=True, verbose_name='介绍')),
                ('signin', models.CharField(max_length=10, null=True, verbose_name='签名')),
                ('tag', models.CharField(max_length=10, null=True, verbose_name='标签')),
                ('createTime', models.CharField(max_length=10, null=True, verbose_name='创建时间')),
                ('updateTime', models.CharField(max_length=10, null=True, verbose_name='修改时间')),
                ('deleteTime', models.CharField(max_length=10, null=True, verbose_name='删除时间')),
                ('recentlyLoginSite', models.CharField(max_length=20, null=True, verbose_name='最近登录地点')),
                ('token', models.CharField(max_length=80, null=True, verbose_name='token')),
                ('ip', models.CharField(max_length=20, null=True, verbose_name='登录ip')),
                ('status', models.IntegerField(default=1, null=True, verbose_name='用户状态')),
                ('isDelete', models.IntegerField(default=0, null=True, verbose_name='删除状态')),
                ('isShow', models.IntegerField(default=0, null=True, verbose_name='显示状态')),
                ('create_by', models.CharField(max_length=20, null=True, verbose_name='创建人')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('picturePath', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.filesave', verbose_name='文件id')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户表',
                'verbose_name_plural': '用户表',
                'db_table': 'stack_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
