# Generated by Django 2.2.7 on 2019-12-06 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20191206_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]