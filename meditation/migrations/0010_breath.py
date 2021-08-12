# Generated by Django 3.2.3 on 2021-06-02 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meditation', '0009_theme'),
    ]

    operations = [
        migrations.CreateModel(
            name='Breath',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('tool_tip', models.CharField(max_length=500)),
                ('thumbnail', models.ImageField(default='themes/placeholder.png', upload_to='themes')),
                ('breath_ratio', models.CharField(max_length=7)),
            ],
        ),
    ]