# Generated by Django 3.1 on 2020-08-06 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mobil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merk', models.CharField(max_length=60)),
                ('nama', models.CharField(max_length=60)),
                ('tahun', models.IntegerField()),
                ('harga', models.IntegerField()),
            ],
        ),
    ]