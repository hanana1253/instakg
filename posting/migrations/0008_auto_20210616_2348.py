# Generated by Django 3.2.4 on 2021-06-16 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0007_auto_20210616_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.TextField(default=1623887302.1965702),
        ),
        migrations.AlterField(
            model_name='posting',
            name='created_at',
            field=models.TextField(default=1623887302.1965702),
        ),
    ]
