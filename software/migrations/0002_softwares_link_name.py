# Generated by Django 2.2.7 on 2019-12-08 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='softwares',
            name='link_name',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]