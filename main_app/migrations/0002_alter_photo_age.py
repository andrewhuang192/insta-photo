# Generated by Django 3.2.3 on 2021-05-17 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='age',
            field=models.IntegerField(),
        ),
    ]
