# Generated by Django 3.1.1 on 2021-03-10 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20210310_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]