# Generated by Django 2.2 on 2019-09-18 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video_upload', '0006_auto_20190918_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeleteTv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TV', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video_upload.Television')),
            ],
        ),
    ]
