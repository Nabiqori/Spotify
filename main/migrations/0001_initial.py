# Generated by Django 5.1.7 on 2025-03-14 08:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('sana', models.DateField()),
                ('rasm', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Qoshiqchi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=255)),
                ('davlat', models.CharField(max_length=255)),
                ('t_sana', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jadval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('janr', models.CharField(max_length=255)),
                ('davomiylik', models.DurationField()),
                ('fayl', models.FileField(blank=True, null=True, upload_to='')),
                ('albom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.albom')),
            ],
        ),
        migrations.AddField(
            model_name='albom',
            name='qoshiqchi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.qoshiqchi'),
        ),
    ]
