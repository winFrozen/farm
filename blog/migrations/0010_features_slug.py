# Generated by Django 4.2.6 on 2024-01-02 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='features',
            name='slug',
            field=models.SlugField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]