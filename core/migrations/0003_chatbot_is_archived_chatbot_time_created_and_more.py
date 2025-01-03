# Generated by Django 5.1.4 on 2024-12-17 18:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_chatbot_id_alter_generalquery_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatbot',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='chatbot',
            name='time_created',
            field=models.TimeField(default=datetime.datetime(2024, 12, 17, 18, 30, 14, 217851, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='generalquery',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='generalquery',
            name='time_created',
            field=models.TimeField(default=datetime.datetime(2024, 12, 17, 18, 30, 14, 218414, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='generalresponse',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='generalresponse',
            name='time_created',
            field=models.TimeField(default=datetime.datetime(2024, 12, 17, 18, 30, 14, 219222, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='reportquery',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reportquery',
            name='time_created',
            field=models.TimeField(default=datetime.datetime(2024, 12, 17, 18, 30, 14, 218838, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='reportresponse',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reportresponse',
            name='time_created',
            field=models.TimeField(default=datetime.datetime(2024, 12, 17, 18, 30, 14, 219601, tzinfo=datetime.timezone.utc)),
        ),
    ]
