# Generated by Django 3.2.9 on 2021-12-29 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0003_alter_order_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listofcomodity',
            old_name='image',
            new_name='thumbnail',
        ),
    ]
