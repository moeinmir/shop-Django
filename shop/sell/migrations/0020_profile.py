# Generated by Django 3.2.9 on 2022-01-07 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sell', '0019_auto_20220106_2008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads')),
                ('address', models.CharField(max_length=255)),
                ('firs_name', models.CharField(max_length=255)),
                ('profession', models.CharField(max_length=255)),
                ('interest', models.CharField(max_length=255)),
                ('costumer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
