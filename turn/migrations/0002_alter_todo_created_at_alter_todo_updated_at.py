# Generated by Django 4.2.5 on 2023-10-30 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]