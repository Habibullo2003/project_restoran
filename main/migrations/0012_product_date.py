# Generated by Django 4.2.1 on 2023-06-19 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_product_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date'),
            preserve_default=False,
        ),
    ]