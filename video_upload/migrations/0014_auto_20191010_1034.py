# Generated by Django 2.2 on 2019-10-10 14:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('video_upload', '0013_auto_20191008_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='upload_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.localtime),
        ),
    ]
