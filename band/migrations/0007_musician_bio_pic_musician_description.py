# Generated by Django 5.2.1 on 2025-06-17 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('band', '0006_venue_description_venue_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='bio_pic',
            field=models.ImageField(blank=True, null=True, upload_to='musicians/'),
        ),
        migrations.AddField(
            model_name='musician',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
