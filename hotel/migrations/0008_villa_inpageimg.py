# Generated by Django 4.0.2 on 2023-06-21 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_food_page_info1_food_page_info2'),
    ]

    operations = [
        migrations.AddField(
            model_name='villa',
            name='inpageimg',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]
