# Generated by Django 4.0.3 on 2022-12-13 00:14

from django.db import migrations, models
import file_uploads.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='', max_length=100)),
                ('number', models.IntegerField()),
                ('unique_identifier', models.UUIDField(default=uuid.uuid4)),
                ('file', models.FileField(upload_to=file_uploads.models.custom_path)),
                ('time_uploaded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
