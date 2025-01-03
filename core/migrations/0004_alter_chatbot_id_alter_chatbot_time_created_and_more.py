# Generated by Django 5.1.4 on 2024-12-17 22:27

import datetime
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_chatbot_is_archived_chatbot_time_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatbot',
            name='id',
            field=models.UUIDField(default=uuid.UUID('43b7a3e1-fd4d-4dfe-907f-4c1923b3399d'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='chatbot',
            name='time_created',
            field=models.TimeField(default=datetime.datetime(2024, 12, 17, 22, 27, 36, 999668, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='generalquery',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b6d35c56-5995-47ad-84fe-13842ea5f028'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='generalquery',
            name='time_created',
            field=models.TimeField(default=datetime.datetime(2024, 12, 17, 22, 27, 37, 49, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='generalresponse',
            name='id',
            field=models.UUIDField(default=uuid.UUID('baa5733f-d332-47a9-a1ae-15a894766846'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='generalresponse',
            name='time_created',
            field=models.TimeField(default=datetime.datetime(2024, 12, 17, 22, 27, 37, 507, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='reportquery',
            name='id',
            field=models.UUIDField(default=uuid.UUID('224e84b2-e41b-40ba-b4bd-717f9345f642'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reportquery',
            name='time_created',
            field=models.TimeField(default=datetime.datetime(2024, 12, 17, 22, 27, 37, 288, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='reportresponse',
            name='id',
            field=models.UUIDField(default=uuid.UUID('01fad8c2-4143-4c2f-bf42-be0affc70f3f'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reportresponse',
            name='time_created',
            field=models.TimeField(default=datetime.datetime(2024, 12, 17, 22, 27, 37, 727, tzinfo=datetime.timezone.utc)),
        ),
    ]
