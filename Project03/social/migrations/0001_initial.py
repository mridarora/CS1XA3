# Generated by Django 2.1.15 on 2020-04-23 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('label', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=280)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('employment', models.CharField(default='Unspecified', max_length=30)),
                ('location', models.CharField(default='Unspecified', max_length=50)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('friends', models.ManyToManyField(related_name='_userinfo_friends_+', to='social.UserInfo')),
                ('interests', models.ManyToManyField(to='social.Interest')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to='social.UserInfo'),
        ),
        migrations.AddField(
            model_name='post',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.UserInfo'),
        ),
        migrations.AddField(
            model_name='friendrequest',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_users', to='social.UserInfo'),
        ),
        migrations.AddField(
            model_name='friendrequest',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_users', to='social.UserInfo'),
        ),
    ]