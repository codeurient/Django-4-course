# Generated by Django 5.0.4 on 2024-06-10 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'ordering': ('id',), 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]