# Generated by Django 4.0.2 on 2023-06-29 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0016_villa_page_info_en_villa_page_info_tr'),
    ]

    operations = [
        migrations.CreateModel(
            name='mainslide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='')),
            ],
        ),
    ]
