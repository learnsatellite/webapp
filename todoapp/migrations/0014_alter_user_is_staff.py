# Generated by Django 5.0.6 on 2024-08-08 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0013_alter_task_options_alter_user_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='管理サイトへのアクセス権限'),
        ),
    ]
