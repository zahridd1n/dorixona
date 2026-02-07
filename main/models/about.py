from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from main.models.titles import BaseTitle


class About(BaseTitle):
    mini_title_uz = models.CharField(max_length=300, verbose_name="mini matnlarni kiriitng UZB")
    mini_title_ru = models.CharField(max_length=300, verbose_name="mini matnlarni kiriitng RUS")
    mini_title_en = models.CharField(max_length=300, verbose_name="mini matnlarni kiriitng ENG")
    description_uz = RichTextUploadingField(verbose_name="Kompaniya haqida batafsil matnlarni kiriting uzb")
    description_ru = RichTextUploadingField(verbose_name="Kompaniya haqida batafsil matnlarni kiriting rus")
    description_en = RichTextUploadingField(verbose_name="Kompaniya haqida batafsil matnlarni kiriting eng")
    image = models.ImageField(upload_to="about/image")

    class Meta:
        verbose_name = "🏢 Kompaniya haqida"
        verbose_name_plural = "🏢 Kompaniya haqida"

    def __str__(self):
        return self.mini_title_uz


class MiniAbout(BaseTitle):
    subtitle_uz = models.TextField(verbose_name="Sarlavha uzbek tilida (to'liq matn)")
    subtitle_ru = models.TextField(verbose_name="Sarlavha rus tilida (to'liq matn)")
    subtitle_en = models.TextField(verbose_name="Sarlavha ingliz tilida (to'liq matn)")
    image = models.ImageField(upload_to="about/image")

    class Meta:
        verbose_name = "🏢 Haqimizda — qo'shimcha"
        verbose_name_plural = "🏢 Haqimizda — qo'shimchalar"


class Socials(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ijtimoiy sahifa nomini kiriitng")
    link = models.CharField(max_length=100, verbose_name="Ijtimoiy sahifa linkini kiriitng")
    icon = models.ImageField(upload_to="about/icon")

    class Meta:
        verbose_name = "🌐 Ijtimoiy tarmoq"
        verbose_name_plural = "🌐 Ijtimoiy tarmoqlar"