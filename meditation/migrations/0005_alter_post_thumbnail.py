# Generated by Django 3.2.3 on 2021-05-25 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meditation', '0004_post_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default='meditation/placeholder.png', null=True, upload_to='meditation/images'),
        ),
    ]
