# Generated by Django 3.2.4 on 2021-06-18 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0011_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='client.category'),
        ),
    ]
