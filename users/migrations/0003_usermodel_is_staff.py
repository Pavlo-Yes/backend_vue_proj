# Generated by Django 3.1.4 on 2020-12-03 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201203_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]
