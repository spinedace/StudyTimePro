# Generated by Django 4.2.7 on 2023-11-06 16:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('STP', '0005_alter_task_options_task_due_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['complete']},
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 7, 16, 40, 33, 568813, tzinfo=datetime.timezone.utc)),
        ),
    ]
