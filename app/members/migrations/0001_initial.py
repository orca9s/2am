# Generated by Django 2.0.6 on 2018-06-19 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('block_users', models.ManyToManyField(blank=True, related_name='block_friends', to='members.BlogUser')),
                ('following', models.ManyToManyField(blank=True, related_name='my_friends', to='members.BlogUser')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=11)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='members.BlogUser')),
            ],
        ),
    ]
