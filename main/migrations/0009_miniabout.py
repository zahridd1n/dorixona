# Generated by Django 5.1.2 on 2024-12-13 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='MiniAbout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(max_length=100, verbose_name='Kichik Sarlavha uzbek tilida')),
                ('title_ru', models.CharField(max_length=100, verbose_name='Kichik Sarlavha rus tilida')),
                ('title_en', models.CharField(max_length=100, verbose_name='Kichik Sarlavha ingliz tilida')),
                ('subtitle_uz', models.TextField(verbose_name="Sarlavha uzbek tilida (to'liq matn)")),
                ('subtitle_ru', models.TextField(verbose_name="Sarlavha rus tilida (to'liq matn)")),
                ('subtitle_en', models.TextField(verbose_name="Sarlavha ingliz tilida (to'liq matn)")),
                ('image', models.ImageField(upload_to='about/image')),
            ],
            options={
                'verbose_name': 'Haqimizda sahifasi uchun qoshimchalar',
                'verbose_name_plural': 'Haqimizda sahifasi uchun qoshimchalar',
            },
        ),
    ]
