# Generated by Django 3.0.8 on 2020-08-08 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0004_remove_tujuan_nama'),
    ]

    operations = [
        migrations.AddField(
            model_name='tujuan',
            name='nama',
            field=models.CharField(default='', max_length=60),
        ),
    ]
