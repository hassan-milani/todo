# Generated by Django 4.1.4 on 2023-07-12 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]