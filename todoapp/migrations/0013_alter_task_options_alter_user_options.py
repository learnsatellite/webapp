# Generated by Django 5.0.6 on 2024-08-08 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0012_alter_user_is_active_alter_user_is_staff'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['completed'], 'verbose_name': 'タスク', 'verbose_name_plural': 'タスク'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'ユーザー', 'verbose_name_plural': 'ユーザー'},
        ),
    ]
