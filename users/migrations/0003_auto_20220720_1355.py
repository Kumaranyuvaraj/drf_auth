# Generated by Django 3.1.2 on 2022-07-20 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, null=True, unique=True, verbose_name='username'),
        ),
    ]