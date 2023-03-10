# Generated by Django 4.1.5 on 2023-02-03 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('mobile', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('date', models.DateField()),
                ('payment', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(max_length=100, null=True)),
                ('quantity', models.IntegerField()),
                ('unit', models.IntegerField()),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
