# Generated by Django 3.1.7 on 2021-03-01 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail_sender', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
                ('date_start', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]