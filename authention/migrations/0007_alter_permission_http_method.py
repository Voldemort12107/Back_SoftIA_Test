# Generated by Django 4.1.3 on 2022-12-04 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authention', '0006_alter_user_role_alter_user_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='http_method',
            field=models.CharField(choices=[('LOCK', 'lock'), ('GET', 'get'), ('PUT', 'put')], max_length=10, verbose_name='Methode'),
        ),
    ]
