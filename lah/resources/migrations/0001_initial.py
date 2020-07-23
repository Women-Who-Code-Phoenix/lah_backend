# Generated by Django 3.0.8 on 2020-07-23 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=528)),
                ('name', models.CharField(max_length=256)),
                ('status', models.CharField(choices=[('active', 'Active'), ('pending', 'Pending')], default='active', max_length=16)),
            ],
        ),
    ]
