# Generated by Django 4.0.3 on 2022-04-17 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0008_auto_20220412_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pictures',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
