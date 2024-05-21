# Generated by Django 4.0.10 on 2024-05-21 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_record_album_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='album_images/'),
        ),
        migrations.AlterField(
            model_name='record',
            name='album_name',
            field=models.CharField(max_length=100),
        ),
    ]
