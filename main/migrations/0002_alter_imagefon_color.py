# Generated by Django 5.1.2 on 2024-12-13 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagefon',
            name='color',
            field=models.CharField(max_length=25, verbose_name='Rang'),
        ),
    ]
