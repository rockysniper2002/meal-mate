# Generated by Django 5.1.7 on 2025-03-30 18:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0002_restaurant'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('picture', models.URLField(default='https://cwdaust.com.au/wpress/wp-content/uploads/2015/04/placeholder-restaurant.png')),
                ('description', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('is_veg', models.BooleanField(default=True)),
                ('retaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='delivery.restaurant')),
            ],
        ),
    ]
