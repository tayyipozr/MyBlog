# Generated by Django 2.2.7 on 2019-12-08 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0002_softwares_link_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='softwares',
            name='size',
            field=models.CharField(max_length=8),
        ),
    ]