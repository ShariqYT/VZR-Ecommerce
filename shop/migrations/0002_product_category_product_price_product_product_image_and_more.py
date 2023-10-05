# Generated by Django 4.2.5 on 2023-10-01 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='subCategory',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(default=0, max_length=50),
        ),
    ]