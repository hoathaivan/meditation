# Generated by Django 3.2.3 on 2021-06-02 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meditation', '0013_breath_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='thumbnail',
            field=models.ImageField(default='themes/thumbnails/placeholder.png', upload_to='themes/thumbnails'),
        ),
    ]
