# Generated by Django 3.0.5 on 2020-04-06 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200405_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file_video',
            field=models.FileField(blank=True, default='', upload_to='media/files/', verbose_name='Видео'),
        ),
    ]