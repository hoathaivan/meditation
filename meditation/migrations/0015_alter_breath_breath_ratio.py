# Generated by Django 3.2.3 on 2021-06-03 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meditation', '0014_theme_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breath',
            name='breath_ratio',
            field=models.CharField(max_length=40),
        ),
    ]