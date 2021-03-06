# Generated by Django 4.0.5 on 2022-06-06 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Iata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=7)),
            ],
            options={
                'db_table': 'iatas',
            },
        ),
        migrations.CreateModel(
            name='Icao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=7)),
            ],
            options={
                'db_table': 'icaos',
            },
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('latitude', models.DecimalField(decimal_places=10, default=0.0, max_digits=20)),
                ('longitude', models.DecimalField(decimal_places=10, default=0.0, max_digits=20)),
                ('elevation', models.IntegerField()),
                ('tz', models.CharField(max_length=20)),
                ('iata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.iata')),
                ('icao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.icao')),
            ],
            options={
                'db_table': 'airports',
            },
        ),
    ]
