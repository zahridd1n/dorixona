# Generated by Django 5.1.2 on 2024-12-24 16:01

import ckeditor_uploader.fields
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(max_length=100, verbose_name='Kichik Sarlavha uzbek tilida')),
                ('title_ru', models.CharField(max_length=100, verbose_name='Kichik Sarlavha rus tilida')),
                ('title_en', models.CharField(max_length=100, verbose_name='Kichik Sarlavha ingliz tilida')),
                ('subtitle_uz', models.CharField(max_length=100, verbose_name='Sarlavha uzbek tilida')),
                ('subtitle_ru', models.CharField(max_length=100, verbose_name='Sarlavha rus tilida')),
                ('subtitle_en', models.CharField(max_length=100, verbose_name='Sarlavha ingliz tilida')),
                ('mini_title_uz', models.CharField(max_length=300, verbose_name='mini matnlarni kiriitng UZB')),
                ('mini_title_ru', models.CharField(max_length=300, verbose_name='mini matnlarni kiriitng RUS')),
                ('mini_title_en', models.CharField(max_length=300, verbose_name='mini matnlarni kiriitng ENG')),
                ('description_uz', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Kompaniya haqida batafsil matnlarni kiriting uzb')),
                ('description_ru', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Kompaniya haqida batafsil matnlarni kiriting uzb')),
                ('description_en', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Kompaniya haqida batafsil matnlarni kiriting uzb')),
                ('image', models.ImageField(upload_to='about/image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='About_offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(max_length=100, verbose_name='Kichik Sarlavha uzbek tilida')),
                ('title_ru', models.CharField(max_length=100, verbose_name='Kichik Sarlavha rus tilida')),
                ('title_en', models.CharField(max_length=100, verbose_name='Kichik Sarlavha ingliz tilida')),
                ('subtitle_uz', models.CharField(max_length=100, verbose_name='Sarlavha uzbek tilida')),
                ('subtitle_ru', models.CharField(max_length=100, verbose_name='Sarlavha rus tilida')),
                ('subtitle_en', models.CharField(max_length=100, verbose_name='Sarlavha ingliz tilida')),
                ('icon', models.ImageField(upload_to='offers/icon', verbose_name='Icon biriktiring')),
            ],
            options={
                'verbose_name': 'About sahifasi uchun offers',
                'verbose_name_plural': 'About sahifasi uchun offers',
            },
        ),
        migrations.CreateModel(
            name='AboutOfferTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(max_length=100, verbose_name='Kichik Sarlavha uzbek tilida')),
                ('title_ru', models.CharField(max_length=100, verbose_name='Kichik Sarlavha rus tilida')),
                ('title_en', models.CharField(max_length=100, verbose_name='Kichik Sarlavha ingliz tilida')),
                ('subtitle_uz', models.CharField(max_length=100, verbose_name='Sarlavha uzbek tilida')),
                ('subtitle_ru', models.CharField(max_length=100, verbose_name='Sarlavha rus tilida')),
                ('subtitle_en', models.CharField(max_length=100, verbose_name='Sarlavha ingliz tilida')),
            ],
            options={
                'verbose_name': 'Sarlavha Haqimizda ustunligimiz ',
                'verbose_name_plural': 'Sarlavha Haqimizda ustunligimiz ',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blog/image', verbose_name='Blog asosiy rasmini kiriting')),
                ('title_uz', models.CharField(max_length=200, verbose_name='Blog sarlavhasini kiriting UZB')),
                ('title_ru', models.CharField(max_length=200, verbose_name='Blog sarlavhasini kiriting RUS')),
                ('title_en', models.CharField(max_length=200, verbose_name='Blog sarlavhasini kiriting ENG')),
                ('description_uz', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Blog matnini kiriting uz tilida')),
                ('description_ru', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Blog matnini kiriting ru tilida')),
                ('description_en', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Blog matnini kiriting en tilida')),
                ('is_active', models.BooleanField(default=False, verbose_name="Asosiy sahifada ko'rinishi uchun aktivlashtiring")),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Bu yerga hech nima yozilmasin ')),
            ],
            options={
                'verbose_name': 'Bloglar',
                'verbose_name_plural': 'Bloglar',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Mijoz ismi')),
                ('phone', models.CharField(max_length=25, verbose_name='Telefon raqami')),
                ('active', models.BooleanField(default=False, verbose_name="Bog'lanib bo'lgandan kn aktivlashtiring")),
            ],
            options={
                'verbose_name': 'Mijozlar arizalari',
                'verbose_name_plural': 'Mijozlar arizalari',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=200, verbose_name='Mijoz ismi uz tilida')),
                ('name_ru', models.CharField(max_length=200, verbose_name='Mijoz ismi uz tilida')),
                ('comment_uz', models.TextField(verbose_name='Izoh matni uz tilida')),
                ('comment_ru', models.TextField(verbose_name='Izoh matni ru tilida')),
                ('comment_en', models.TextField(verbose_name='Izoh matni en tilida')),
                ('additional_uz', models.CharField(max_length=200, verbose_name="Qo'shimcha uz tilida")),
                ('additional_ru', models.CharField(max_length=200, verbose_name="Qo'shimca ru tilida")),
                ('additional_en', models.CharField(max_length=200, verbose_name="Qo'shimca en tilida")),
                ('image', models.ImageField(upload_to='comments/image')),
            ],
            options={
                'verbose_name': 'Mijozlar izohi',
                'verbose_name_plural': 'Mijozlar izohi',
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_uz', models.CharField(max_length=200, verbose_name='Savol Matni uz tilida')),
                ('question_ru', models.CharField(max_length=200, verbose_name='Savol Matni ru tilida')),
                ('question_en', models.CharField(max_length=200, verbose_name='Savol Matni en tilida')),
                ('answer_uz', models.CharField(max_length=200, verbose_name='Javob matni uz tilida')),
                ('answer_ru', models.CharField(max_length=200, verbose_name='Javob matni ru tilida')),
                ('answer_en', models.CharField(max_length=200, verbose_name='Javob matni en tilida')),
            ],
            options={
                'verbose_name': 'FAQ Savol va Javolari',
                'verbose_name_plural': 'FAQ Savol va Javolari',
            },
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(max_length=100, verbose_name='Kichik Sarlavha uzbek tilida')),
                ('title_ru', models.CharField(max_length=100, verbose_name='Kichik Sarlavha rus tilida')),
                ('title_en', models.CharField(max_length=100, verbose_name='Kichik Sarlavha ingliz tilida')),
                ('subtitle_uz', models.CharField(max_length=100, verbose_name='Sarlavha uzbek tilida')),
                ('subtitle_ru', models.CharField(max_length=100, verbose_name='Sarlavha rus tilida')),
                ('subtitle_en', models.CharField(max_length=100, verbose_name='Sarlavha ingliz tilida')),
                ('logo', models.ImageField(upload_to='blog/image', verbose_name='Logo rasmini kiriting png holatda')),
                ('mini_text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Saytning eng pastidagi matnni kiriting')),
                ('phone', models.CharField(max_length=15, verbose_name='Telefon raqam kiriting')),
                ('address_uz', models.CharField(max_length=50, verbose_name='Manzilni kiriting UZB')),
                ('address_ru', models.CharField(max_length=50, verbose_name='Manzilni kiriting RUS')),
                ('address_en', models.CharField(max_length=50, verbose_name='Manzilni kiriting ENG')),
            ],
            options={
                'verbose_name': 'Footer',
                'verbose_name_plural': 'Footer',
            },
        ),
        migrations.CreateModel(
            name='ImageFon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nomi')),
                ('color', models.CharField(max_length=25, verbose_name='Rang')),
            ],
            options={
                'verbose_name': 'Fon rasmi',
                'verbose_name_plural': 'Fon rasmlari',
            },
        ),
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
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=100, verbose_name='Nomlanishi uz tilida')),
                ('name_ru', models.CharField(max_length=100, verbose_name='Nomlanishi ru tilida')),
                ('name_en', models.CharField(max_length=100, verbose_name='Nomlanishi en tilida')),
                ('total', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99999)], verbose_name='Raqamlarda kiriting')),
                ('icon', models.ImageField(upload_to='offers/icon', verbose_name='icon biriktiring')),
            ],
            options={
                'verbose_name': 'Yutuqlarimiz',
                'verbose_name_plural': 'Yutuqlarimiz',
            },
        ),
        migrations.CreateModel(
            name='Offers2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(max_length=100, verbose_name='Kichik Sarlavha uzbek tilida')),
                ('title_ru', models.CharField(max_length=100, verbose_name='Kichik Sarlavha rus tilida')),
                ('title_en', models.CharField(max_length=100, verbose_name='Kichik Sarlavha ingliz tilida')),
                ('subtitle_uz', models.CharField(max_length=100, verbose_name='Sarlavha uzbek tilida')),
                ('subtitle_ru', models.CharField(max_length=100, verbose_name='Sarlavha rus tilida')),
                ('subtitle_en', models.CharField(max_length=100, verbose_name='Sarlavha ingliz tilida')),
                ('icon', models.ImageField(upload_to='offers/icon', verbose_name='Icon biriktiring')),
            ],
            options={
                'verbose_name': 'Yutuqlarimiz2',
                'verbose_name_plural': 'Yutuqlarimiz2',
            },
        ),
        migrations.CreateModel(
            name='Socials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ijtimoiy sahifa nomini kiriitng')),
                ('link', models.CharField(max_length=100, verbose_name='Ijtimoiy sahifa linkini kiriitng')),
                ('icon', models.ImageField(upload_to='about/icon')),
            ],
            options={
                'verbose_name': 'Ijtimoiy sahifa',
                'verbose_name_plural': 'Ijtimoiy sahifa',
            },
        ),
        migrations.CreateModel(
            name='TitleAbout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(max_length=100, verbose_name='Kichik Sarlavha uzbek tilida')),
                ('title_ru', models.CharField(max_length=100, verbose_name='Kichik Sarlavha rus tilida')),
                ('title_en', models.CharField(max_length=100, verbose_name='Kichik Sarlavha ingliz tilida')),
                ('subtitle_uz', models.CharField(max_length=100, verbose_name='Sarlavha uzbek tilida')),
                ('subtitle_ru', models.CharField(max_length=100, verbose_name='Sarlavha rus tilida')),
                ('subtitle_en', models.CharField(max_length=100, verbose_name='Sarlavha ingliz tilida')),
            ],
            options={
                'verbose_name': 'Sarlavha Haqimizda',
                'verbose_name_plural': 'Sarlavha Haqimizda',
            },
        ),
        migrations.CreateModel(
            name='TitleBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(max_length=100, verbose_name='Kichik Sarlavha uzbek tilida')),
                ('title_ru', models.CharField(max_length=100, verbose_name='Kichik Sarlavha rus tilida')),
                ('title_en', models.CharField(max_length=100, verbose_name='Kichik Sarlavha ingliz tilida')),
                ('subtitle_uz', models.CharField(max_length=100, verbose_name='Sarlavha uzbek tilida')),
                ('subtitle_ru', models.CharField(max_length=100, verbose_name='Sarlavha rus tilida')),
                ('subtitle_en', models.CharField(max_length=100, verbose_name='Sarlavha ingliz tilida')),
            ],
            options={
                'verbose_name': 'Sarlavha Banner',
                'verbose_name_plural': 'Sarlavha Banner',
            },
        ),
        migrations.CreateModel(
            name='TitleBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(max_length=100, verbose_name='Kichik Sarlavha uzbek tilida')),
                ('title_ru', models.CharField(max_length=100, verbose_name='Kichik Sarlavha rus tilida')),
                ('title_en', models.CharField(max_length=100, verbose_name='Kichik Sarlavha ingliz tilida')),
                ('subtitle_uz', models.CharField(max_length=100, verbose_name='Sarlavha uzbek tilida')),
                ('subtitle_ru', models.CharField(max_length=100, verbose_name='Sarlavha rus tilida')),
                ('subtitle_en', models.CharField(max_length=100, verbose_name='Sarlavha ingliz tilida')),
            ],
            options={
                'verbose_name': 'Sarlavha Maqolalar',
                'verbose_name_plural': 'Sarlavha Maqolalar',
            },
        ),
        migrations.CreateModel(
            name='TitleComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(max_length=100, verbose_name='Kichik Sarlavha uzbek tilida')),
                ('title_ru', models.CharField(max_length=100, verbose_name='Kichik Sarlavha rus tilida')),
                ('title_en', models.CharField(max_length=100, verbose_name='Kichik Sarlavha ingliz tilida')),
                ('subtitle_uz', models.CharField(max_length=100, verbose_name='Sarlavha uzbek tilida')),
                ('subtitle_ru', models.CharField(max_length=100, verbose_name='Sarlavha rus tilida')),
                ('subtitle_en', models.CharField(max_length=100, verbose_name='Sarlavha ingliz tilida')),
            ],
            options={
                'verbose_name': 'Sarlavha Mijozlar fikri',
                'verbose_name_plural': 'Sarlavha Mijozlar fikri',
            },
        ),
        migrations.CreateModel(
            name='TitleContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(max_length=100, verbose_name='Kichik Sarlavha uzbek tilida')),
                ('title_ru', models.CharField(max_length=100, verbose_name='Kichik Sarlavha rus tilida')),
                ('title_en', models.CharField(max_length=100, verbose_name='Kichik Sarlavha ingliz tilida')),
                ('subtitle_uz', models.CharField(max_length=100, verbose_name='Sarlavha uzbek tilida')),
                ('subtitle_ru', models.CharField(max_length=100, verbose_name='Sarlavha rus tilida')),
                ('subtitle_en', models.CharField(max_length=100, verbose_name='Sarlavha ingliz tilida')),
            ],
            options={
                'verbose_name': 'Sarlavha Kontakt',
                'verbose_name_plural': 'Sarlavha Kontakt',
            },
        ),
        migrations.CreateModel(
            name='TitleFaq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(max_length=100, verbose_name='Kichik Sarlavha uzbek tilida')),
                ('title_ru', models.CharField(max_length=100, verbose_name='Kichik Sarlavha rus tilida')),
                ('title_en', models.CharField(max_length=100, verbose_name='Kichik Sarlavha ingliz tilida')),
                ('subtitle_uz', models.CharField(max_length=100, verbose_name='Sarlavha uzbek tilida')),
                ('subtitle_ru', models.CharField(max_length=100, verbose_name='Sarlavha rus tilida')),
                ('subtitle_en', models.CharField(max_length=100, verbose_name='Sarlavha ingliz tilida')),
                ('image', models.ImageField(upload_to='faq/icons', verbose_name='FAQ icon')),
            ],
            options={
                'verbose_name': 'Sarlavha FAQ',
                'verbose_name_plural': 'Sarlavha FAQ',
            },
        ),
        migrations.CreateModel(
            name='TitleHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(max_length=100, verbose_name='Kichik Sarlavha uzbek tilida')),
                ('title_ru', models.CharField(max_length=100, verbose_name='Kichik Sarlavha rus tilida')),
                ('title_en', models.CharField(max_length=100, verbose_name='Kichik Sarlavha ingliz tilida')),
                ('subtitle_uz', models.CharField(max_length=100, verbose_name='Sarlavha uzbek tilida')),
                ('subtitle_ru', models.CharField(max_length=100, verbose_name='Sarlavha rus tilida')),
                ('subtitle_en', models.CharField(max_length=100, verbose_name='Sarlavha ingliz tilida')),
            ],
            options={
                'verbose_name': "Sarlavha Bo'sh bo'lim sahifasi",
                'verbose_name_plural': "Sarlavha Bo'sh bo'lim sahifasi",
            },
        ),
        migrations.CreateModel(
            name='TitleOffers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(max_length=100, verbose_name='Kichik Sarlavha uzbek tilida')),
                ('title_ru', models.CharField(max_length=100, verbose_name='Kichik Sarlavha rus tilida')),
                ('title_en', models.CharField(max_length=100, verbose_name='Kichik Sarlavha ingliz tilida')),
                ('subtitle_uz', models.CharField(max_length=100, verbose_name='Sarlavha uzbek tilida')),
                ('subtitle_ru', models.CharField(max_length=100, verbose_name='Sarlavha rus tilida')),
                ('subtitle_en', models.CharField(max_length=100, verbose_name='Sarlavha ingliz tilida')),
            ],
            options={
                'verbose_name': 'Sarlavha Ustunligimiz',
                'verbose_name_plural': 'Sarlavha Ustunligimiz',
            },
        ),
        migrations.CreateModel(
            name='TitleProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(max_length=100, verbose_name='Kichik Sarlavha uzbek tilida')),
                ('title_ru', models.CharField(max_length=100, verbose_name='Kichik Sarlavha rus tilida')),
                ('title_en', models.CharField(max_length=100, verbose_name='Kichik Sarlavha ingliz tilida')),
                ('subtitle_uz', models.CharField(max_length=100, verbose_name='Sarlavha uzbek tilida')),
                ('subtitle_ru', models.CharField(max_length=100, verbose_name='Sarlavha rus tilida')),
                ('subtitle_en', models.CharField(max_length=100, verbose_name='Sarlavha ingliz tilida')),
            ],
            options={
                'verbose_name': 'Sarlavha Mahsulotlar',
                'verbose_name_plural': 'Sarlavha Mahsulotlar',
            },
        ),
        migrations.CreateModel(
            name='TitleProductDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(max_length=100, verbose_name='Kichik Sarlavha uzbek tilida')),
                ('title_ru', models.CharField(max_length=100, verbose_name='Kichik Sarlavha rus tilida')),
                ('title_en', models.CharField(max_length=100, verbose_name='Kichik Sarlavha ingliz tilida')),
                ('subtitle_uz', models.CharField(max_length=100, verbose_name='Sarlavha uzbek tilida')),
                ('subtitle_ru', models.CharField(max_length=100, verbose_name='Sarlavha rus tilida')),
                ('subtitle_en', models.CharField(max_length=100, verbose_name='Sarlavha ingliz tilida')),
            ],
            options={
                'verbose_name': 'Sarlavha Product detail sahifasi',
                'verbose_name_plural': 'Sarlavha Product detail sahifasi',
            },
        ),
        migrations.CreateModel(
            name='TitleVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(max_length=100, verbose_name='Kichik Sarlavha uzbek tilida')),
                ('title_ru', models.CharField(max_length=100, verbose_name='Kichik Sarlavha rus tilida')),
                ('title_en', models.CharField(max_length=100, verbose_name='Kichik Sarlavha ingliz tilida')),
                ('subtitle_uz', models.CharField(max_length=100, verbose_name='Sarlavha uzbek tilida')),
                ('subtitle_ru', models.CharField(max_length=100, verbose_name='Sarlavha rus tilida')),
                ('subtitle_en', models.CharField(max_length=100, verbose_name='Sarlavha ingliz tilida')),
            ],
            options={
                'verbose_name': 'Sarlavha Videolar',
                'verbose_name_plural': 'Sarlavha Videolar',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(max_length=200, verbose_name='Video sarlavhasini kiriting UZB')),
                ('title_ru', models.CharField(max_length=200, verbose_name='Video sarlavhasini kiriting RUS')),
                ('title_en', models.CharField(max_length=200, verbose_name='Video sarlavhasini kiriting ENG')),
                ('image', models.ImageField(upload_to='blog/image', verbose_name='Video uchun asosiy rasmini kiriting')),
                ('is_active', models.BooleanField(default=False, verbose_name="Asosiy sahifada ko'rinishi uchun aktivlashtiring")),
                ('link', models.CharField(max_length=200, verbose_name='Video linkini kiriting')),
            ],
            options={
                'verbose_name': 'Videolar',
                'verbose_name_plural': 'Videolar',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=100, verbose_name='Maxsulot nomi (UZ)')),
                ('name_ru', models.CharField(max_length=100, verbose_name='Maxsulot nomi (RU)')),
                ('name_en', models.CharField(max_length=100, verbose_name='Maxsulot nomi (EN)')),
                ('fields_uz', models.CharField(max_length=200, verbose_name='Xususiyatlari (UZ)')),
                ('fields_ru', models.CharField(max_length=200, verbose_name='Xususiyatlari (RU)')),
                ('fields_en', models.CharField(max_length=200, verbose_name='Xususiyatlari (EN)')),
                ('detailmini_uz', models.TextField(verbose_name='Xususiyatlari (UZ)')),
                ('detailmini_ru', models.TextField(verbose_name='Xususiyatlari (RU)')),
                ('detailmini_en', models.TextField(verbose_name='Xususiyatlari (EN)')),
                ('detail_uz', models.TextField(verbose_name='Mahsulot haqida uz tilida')),
                ('detail_ru', models.TextField(verbose_name='Mahsulot haqida ru tilida')),
                ('detail_en', models.TextField(verbose_name='Mahsulot haqida en tilida')),
                ('content_uz', models.TextField(verbose_name='Mahsulot haqida uz tilida')),
                ('content_ru', models.TextField(verbose_name='Mahsulot haqida ru tilida')),
                ('content_en', models.TextField(verbose_name='Mahsulot haqida en tilida')),
                ('description_uz', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Mahsulot haqida batafsil uz tilida')),
                ('description_ru', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Mahsulot haqida batafsil ru tilida')),
                ('description_en', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Mahsulot haqida batafsil en tilida')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Bu yerga hech nima yozilmasin ')),
                ('active', models.BooleanField(default=False, verbose_name='Asosiy sahifada chiqishini hohlasangiz yoqing')),
                ('image1', models.ImageField(upload_to='product/image')),
                ('image2', models.ImageField(upload_to='product/image')),
                ('image3', models.ImageField(upload_to='product/image')),
                ('image4', models.ImageField(upload_to='product/image')),
                ('background', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.imagefon', verbose_name='Orqa fon')),
            ],
            options={
                'verbose_name': 'Mahsulot',
                'verbose_name_plural': 'Mahsulotlar',
            },
        ),
    ]
