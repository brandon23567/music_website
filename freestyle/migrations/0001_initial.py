# Generated by Django 3.2.7 on 2022-09-07 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadSong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song', models.FileField(upload_to='songs/')),
                ('song_name', models.CharField(max_length=100)),
            ],
        ),
    ]
