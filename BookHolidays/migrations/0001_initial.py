# Generated by Django 3.1.7 on 2021-03-17 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Holidays_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('Department', models.CharField(max_length=50)),
                ('Staff_level', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('staff_level', models.CharField(max_length=50)),
                ('Holidays_taken', models.IntegerField(null=True)),
                ('Holidays_left', models.IntegerField(null=True)),
            ],
        ),
    ]
