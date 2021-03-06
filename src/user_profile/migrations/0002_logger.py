# Generated by Django 2.2.10 on 2020-04-12 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=250)),
                ('method', models.CharField(max_length=50)),
                ('time_delta', models.CharField(max_length=50)),
                ('user_id', models.IntegerField()),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
