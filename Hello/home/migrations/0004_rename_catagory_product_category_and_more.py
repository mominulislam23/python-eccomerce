# Generated by Django 4.0.5 on 2022-06-26 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_product_catagory_product_image_product_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='catagory',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subcatagory',
        ),
        migrations.AddField(
            model_name='product',
            name='subcetagory',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
    ]
