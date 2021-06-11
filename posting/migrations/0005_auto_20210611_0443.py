# Generated by Django 3.2.4 on 2021-06-11 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_profile_created_at'),
        ('posting', '0004_auto_20210610_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.TextField(default=1623386597.2959528),
        ),
        migrations.AlterField(
            model_name='comment',
            name='like_users',
            field=models.ManyToManyField(blank=True, related_name='liked_comments', to='authentication.Profile'),
        ),
        migrations.AlterField(
            model_name='posting',
            name='created_at',
            field=models.TextField(default=1623386597.2959528),
        ),
        migrations.AlterField(
            model_name='posting',
            name='like_users',
            field=models.ManyToManyField(blank=True, related_name='liked_postings', to='authentication.Profile'),
        ),
    ]
