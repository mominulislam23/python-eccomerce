# Generated by Django 4.0.5 on 2022-06-26 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=350)),
                ('product_desc', models.CharField(max_length=50)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
