# Generated by Django 3.0.3 on 2020-03-22 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20200322_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='items_json',
            field=models.CharField(default='', max_length=5000),
        ),
    ]