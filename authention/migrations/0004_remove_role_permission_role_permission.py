# Generated by Django 4.1.3 on 2022-12-03 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authention', '0003_user_groups_user_is_superuser_user_user_permissions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='permission',
        ),
        migrations.AddField(
            model_name='role',
            name='permission',
            field=models.ManyToManyField(to='authention.permission'),
        ),
    ]