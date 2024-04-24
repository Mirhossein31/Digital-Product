# Generated by Django 4.2 on 2024-04-20 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_file_file_type_alter_file_created_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='avator',
        ),
        migrations.RemoveField(
            model_name='product',
            name='avator',
        ),
        migrations.AddField(
            model_name='category',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='categories/', verbose_name='avatar'),
        ),
        migrations.AddField(
            model_name='product',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='products/', verbose_name='avatar'),
        ),
    ]
