# Generated by Django 4.1 on 2022-09-15 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=255)),
                ('item_price', models.BigIntegerField()),
                ('item_stock', models.IntegerField()),
                ('description', models.TextField()),
                ('rating', models.IntegerField()),
                ('item_url', models.URLField()),
            ],
        ),
    ]
