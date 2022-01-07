# Generated by Django 3.1.7 on 2021-11-25 05:51

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=191)),
                ('price', models.TextField(max_length=50)),
                ('description', models.TextField(max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=products.models.filepath)),
            ],
        ),
    ]
