# Generated by Django 3.2.9 on 2022-01-04 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0011_auto_20220104_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketsearch',
            name='status',
            field=models.CharField(choices=[('processing', 'processing'), ('confirmed', 'confirmed'), ('payed', 'payed'), ('all', 'all')], default='all', max_length=55),
        ),
    ]