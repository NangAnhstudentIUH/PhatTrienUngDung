# Generated by Django 4.2.11 on 2024-03-26 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('url', models.URLField()),
                ('redirect_url', models.URLField()),
                ('thumb', models.URLField()),
                ('thumb_l', models.URLField()),
                ('publisher', models.CharField(max_length=255)),
            ],
        ),
    ]