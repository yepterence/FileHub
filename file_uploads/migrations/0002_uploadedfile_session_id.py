# Generated by Django 4.0.3 on 2022-12-13 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_uploads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='session_id',
            field=models.CharField(default='', max_length=100),
        ),
    ]