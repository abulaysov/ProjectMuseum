# Generated by Django 4.0.3 on 2022-04-17 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotes',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
