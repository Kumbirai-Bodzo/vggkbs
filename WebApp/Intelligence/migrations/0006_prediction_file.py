# Generated by Django 3.1.4 on 2021-06-21 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Intelligence', '0005_auto_20210621_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='prediction',
            name='file',
            field=models.FileField(blank=True, upload_to='images/'),
        ),
    ]