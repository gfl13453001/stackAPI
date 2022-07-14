# Generated by Django 3.2.4 on 2021-09-16 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('public', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nav',
            name='icon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.filesave', verbose_name='文件id'),
        ),
        migrations.AddField(
            model_name='banner',
            name='file',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.filesave', verbose_name='文件id'),
        ),
    ]