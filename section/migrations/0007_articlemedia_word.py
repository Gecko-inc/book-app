# Generated by Django 3.1.6 on 2021-09-19 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0006_articlemedia_additional_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlemedia',
            name='word',
            field=models.TextField(blank=True, null=True, verbose_name='Слова'),
        ),
    ]
