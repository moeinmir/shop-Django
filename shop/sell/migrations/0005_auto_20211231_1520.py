# Generated by Django 3.2.9 on 2021-12-31 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0004_rename_image_listofcomodity_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='comment_content',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='related_post',
        ),
        migrations.AlterField(
            model_name='shopbasket',
            name='total_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]