# Generated by Django 3.1.1 on 2020-10-12 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0012_auto_20200928_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='repository',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
