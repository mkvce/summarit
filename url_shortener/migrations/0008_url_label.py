# Generated by Django 3.1.6 on 2021-04-27 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0007_auto_20210427_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='label',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]