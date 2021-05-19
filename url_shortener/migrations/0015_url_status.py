# Generated by Django 3.1.6 on 2021-05-19 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0014_remove_url_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='status',
            field=models.CharField(choices=[('E', 'فعال'), ('D', 'غیر فعال')], default='E', max_length=1, verbose_name='وضعیت'),
        ),
    ]
