# Generated by Django 2.2 on 2019-10-08 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video_upload', '0012_document_upload_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='tv',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tv_table', to='video_upload.Television'),
        ),
    ]
