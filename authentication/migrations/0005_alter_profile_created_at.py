# Generated by Django 3.2.4 on 2021-06-10 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20210610_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.TextField(default=1623318649.729716),
        ),
    ]
