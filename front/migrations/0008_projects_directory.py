# Generated by Django 2.2.13 on 2020-06-23 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0007_auto_20200623_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='directory',
            field=models.CharField(default='', max_length=200, verbose_name='Папка с фотографиями'),
        ),
    ]
