# Generated by Django 3.0.5 on 2020-04-06 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200406_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file_video',
            field=models.FileField(default='', upload_to='documents', verbose_name='Видео'),
        ),
    ]
