# Generated by Django 4.2.13 on 2024-06-20 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, choices=[('option1', '未着手'), ('option2', '作業中'), ('option3', '完了')], max_length=10, null=True),
        ),
    ]
