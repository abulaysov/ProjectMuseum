# Generated by Django 3.1.1 on 2022-04-11 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0005_biographies_era'),
    ]

    operations = [
        migrations.AddField(
            model_name='biographies',
            name='genre',
            field=models.CharField(default='', max_length=50),
        ),
    ]