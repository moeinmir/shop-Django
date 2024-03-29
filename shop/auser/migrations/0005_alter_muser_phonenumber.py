# Generated by Django 3.2.9 on 2021-12-29 19:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auser', '0004_alter_muser_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muser',
            name='phonenumber',
            field=models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
