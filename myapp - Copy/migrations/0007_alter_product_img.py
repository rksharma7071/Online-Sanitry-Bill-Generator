# Generated by Django 4.1.5 on 2023-02-03 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(null=True, upload_to='media/upload'),
        ),
    ]