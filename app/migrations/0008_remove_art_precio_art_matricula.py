# Generated by Django 4.2.11 on 2024-03-23 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_art_options_alter_auto_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='art',
            name='precio',
        ),
        migrations.AddField(
            model_name='art',
            name='matricula',
            field=models.CharField(default='', max_length=40),
        ),
    ]
