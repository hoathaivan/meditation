# Generated by Django 3.2.3 on 2021-06-06 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meditation', '0018_auto_20210606_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='note',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='sub_headline',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
