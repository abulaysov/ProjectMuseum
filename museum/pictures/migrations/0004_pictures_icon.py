# Generated by Django 4.0.3 on 2022-03-23 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0003_pictures_name_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='pictures',
            name='icon',
            field=models.ImageField(default='', upload_to='icon/'),
        ),
    ]
