# Generated by Django 4.0.2 on 2023-06-21 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0008_villa_inpageimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='villa',
            name='inpageimg',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]
