# Generated by Django 5.1.1 on 2024-09-04 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='media',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]
