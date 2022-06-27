# Generated by Django 4.0.5 on 2022-06-26 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='catagory',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=0, upload_to='shop/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='subcatagory',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
