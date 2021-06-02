# Generated by Django 3.2.3 on 2021-06-02 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meditation', '0008_alter_post_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('tool_tip', models.CharField(max_length=500)),
                ('background', models.ImageField(default='themes/placeholder.png', upload_to='themes')),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]