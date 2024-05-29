# Generated by Django 5.0.4 on 2024-04-24 08:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('shopapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='shopapp.product'),
        ),
    ]
