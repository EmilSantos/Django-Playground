# Generated by Django 3.1.7 on 2021-12-14 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.CharField(default='dfs', max_length=220),
            preserve_default=False,
        ),
    ]