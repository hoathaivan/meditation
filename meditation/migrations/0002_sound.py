# Generated by Django 3.2.3 on 2021-05-19 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meditation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('source', models.CharField(max_length=200)),
            ],
        ),
    ]