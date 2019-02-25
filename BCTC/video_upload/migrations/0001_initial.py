# Generated by Django 2.1.5 on 2019-02-22 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('tv', models.CharField(choices=[('TV1', 'TV1'), ('TV2', 'TV2'), ('TV3', 'TV3'), ('TV4', 'TV4')], default='TV1', max_length=3)),
                ('document', models.FileField(upload_to=models.CharField(choices=[('TV1', 'TV1'), ('TV2', 'TV2'), ('TV3', 'TV3'), ('TV4', 'TV4')], default='TV1', max_length=3))),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
