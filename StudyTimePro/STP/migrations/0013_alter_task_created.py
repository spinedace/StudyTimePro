# Generated by Django 4.2.6 on 2023-11-08 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('STP', '0012_alter_task_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateField(),
        ),
    ]
