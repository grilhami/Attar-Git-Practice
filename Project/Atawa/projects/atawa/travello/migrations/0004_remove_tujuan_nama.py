# Generated by Django 3.0.8 on 2020-08-08 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0003_tujuan_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tujuan',
            name='nama',
        ),
    ]