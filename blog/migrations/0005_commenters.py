# Generated by Django 4.2.6 on 2023-12-26 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commenters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('comment', models.TextField()),
                ('img', models.ImageField(upload_to='Commenters/img')),
            ],
        ),
    ]