# Generated by Django 5.1.4 on 2024-12-17 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatbot',
            name='id',
            field=models.UUIDField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='generalquery',
            name='id',
            field=models.UUIDField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='generalresponse',
            name='id',
            field=models.UUIDField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reportquery',
            name='id',
            field=models.UUIDField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reportresponse',
            name='id',
            field=models.UUIDField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
