# Generated by Django 3.1.6 on 2021-04-26 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('جواد زاهدی', models.URLField(max_length=512, verbose_name='آدرس لینک')),
                ('code', models.SlugField(max_length=6, verbose_name='لینک کوتاه')),
                ('visits', models.PositiveIntegerField(default=0, verbose_name='تعداد بازدیدها')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]