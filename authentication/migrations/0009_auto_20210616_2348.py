# Generated by Django 3.2.4 on 2021-06-16 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_auto_20210616_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.TextField(default=1623887302.1965702),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(blank=True, default='profile_pic/close-button-png-30230.png', null=True, upload_to='profile_pic'),
        ),
    ]
