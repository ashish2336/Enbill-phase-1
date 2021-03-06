# Generated by Django 3.0 on 2021-09-09 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marketing_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=60)),
                ('Phone_number', models.CharField(blank=True, error_messages={'unique': 'This mobile no is already registered.'}, max_length=10, null=True, unique=True)),
                ('Address', models.CharField(max_length=60)),
                ('Pincode', models.CharField(max_length=60)),
                ('State', models.CharField(max_length=60)),
                ('Town', models.CharField(max_length=60)),
                ('City', models.CharField(max_length=60)),
            ],
        ),
    ]
