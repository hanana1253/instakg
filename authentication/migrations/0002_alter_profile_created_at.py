# Generated by Django 3.2.4 on 2021-06-10 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.TextField(default=1623299627.448716),
        ),
    ]
