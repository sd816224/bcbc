# Generated by Django 4.2.2 on 2023-11-27 16:44

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=300, null=True, verbose_name='Title')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='shop/thumbnail/')),
                ('description', ckeditor.fields.RichTextField(null=True)),
                ('price', models.IntegerField()),
                ('slug', models.SlugField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Item_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to='shop/')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.item')),
            ],
        ),
    ]