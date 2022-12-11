# Generated by Django 4.0.3 on 2022-12-11 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
                ('file', models.FileField(upload_to='files/')),
                ('time_uploaded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
