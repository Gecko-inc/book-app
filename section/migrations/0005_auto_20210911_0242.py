# Generated by Django 3.1.6 on 2021-09-10 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0004_auto_20210911_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активна'),
        ),
        migrations.AlterField(
            model_name='section',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активна'),
        ),
    ]
