# Generated by Django 3.1.1 on 2022-04-11 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0004_auto_20220411_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='biographies',
            name='era',
            field=models.CharField(default='', max_length=50),
        ),
    ]
