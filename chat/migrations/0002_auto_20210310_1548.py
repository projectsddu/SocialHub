# Generated by Django 3.1.5 on 2021-03-10 10:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('chat_room_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_group', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_room_id', models.IntegerField()),
                ('message', models.TextField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Subcriber',
            new_name='Subscriber',
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
        migrations.RenameField(
            model_name='subscriber',
            old_name='chat_id',
            new_name='chat_room_id',
        ),
        migrations.RenameField(
            model_name='subscriber',
            old_name='subcriber',
            new_name='user_id',
        ),
    ]
