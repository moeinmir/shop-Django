# Generated by Django 3.2.9 on 2022-01-06 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0016_auto_20220106_1321'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasketSearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('processing', 'processing'), ('confirmed', 'confirmed'), ('payed', 'payed'), ('all', 'all')], default='all', max_length=55)),
                ('begin_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]