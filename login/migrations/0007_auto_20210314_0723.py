# Generated by Django 3.1.1 on 2021-03-14 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20210314_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='Image',
            field=models.ImageField(default='media/asset/images/user_default.png', upload_to='home/user_images'),
        ),
    ]