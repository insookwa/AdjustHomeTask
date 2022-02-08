# Generated by Django 4.0.2 on 2022-02-08 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('channel', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=10)),
                ('os', models.CharField(max_length=20)),
                ('impressions', models.IntegerField()),
                ('clicks', models.IntegerField()),
                ('installs', models.IntegerField()),
                ('spend', models.FloatField()),
                ('revenue', models.FloatField()),
            ],
        ),
    ]
