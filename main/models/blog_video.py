from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from main.models.titles import BaseTitle
from django.utils.text import slugify


class Blog(models.Model):
    image = models.ImageField(upload_to="blog/image", verbose_name="Blog asosiy rasmini kiriting")
    title_uz = models.CharField(max_length=200, verbose_name="Blog sarlavhasini kiriting UZB")
    title_ru = models.CharField(max_length=200, verbose_name="Blog sarlavhasini kiriting RUS")
    title_en = models.CharField(max_length=200, verbose_name="Blog sarlavhasini kiriting ENG")
    description_uz = RichTextUploadingField(verbose_name="Blog matnini kiriting uz tilida")
    description_ru = RichTextUploadingField(verbose_name="Blog matnini kiriting ru tilida")
    description_en = RichTextUploadingField(verbose_name="Blog matnini kiriting en tilida")
    is_active = models.BooleanField(default=False, verbose_name="Asosiy sahifada ko'rinishi uchun aktivlashtiring")
    slug = models.SlugField(unique=True, db_index=True, null=True, blank=True, verbose_name="Bu yerga hech nima yozilmasin")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_uz or "default-title")
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "📝 Blog maqola"
        verbose_name_plural = "📝 Blog maqolalar"

    def __str__(self):
        return self.title_uz


class Video(models.Model):
    title_uz = models.CharField(max_length=200, verbose_name="Video sarlavhasini kiriting UZB")
    title_ru = models.CharField(max_length=200, verbose_name="Video sarlavhasini kiriting RUS")
    title_en = models.CharField(max_length=200, verbose_name="Video sarlavhasini kiriting ENG")
    image = models.ImageField(upload_to="blog/image", verbose_name="Video uchun asosiy rasmini kiriting")
    is_active = models.BooleanField(default=False, verbose_name="Asosiy sahifada ko'rinishi uchun aktivlashtiring")
    link = models.CharField(max_length=200, verbose_name="Video linkini kiriting")

    class Meta:
        verbose_name = "🎬 Video"
        verbose_name_plural = "🎬 Videolar"

    def __str__(self):
        return self.title_uz


class Footer(BaseTitle):
    logo = models.ImageField(upload_to="blog/image", verbose_name="Logo rasmini kiriting png holatda")
    mini_text = RichTextUploadingField(verbose_name="Saytning eng pastidagi matnni kiriting")
    phone = models.CharField(max_length=15, verbose_name="Telefon raqam kiriting")
    address_uz = models.CharField(max_length=50, verbose_name="Manzilni kiriting UZB")
    address_ru = models.CharField(max_length=50, verbose_name="Manzilni kiriting RUS")
    address_en = models.CharField(max_length=50, verbose_name="Manzilni kiriting ENG")

    class Meta:
        verbose_name = "🔻 Footer"
        verbose_name_plural = "🔻 Footer"

    def __str__(self):
        return self.title_uz


class Client(models.Model):
    name = models.CharField(max_length=25, verbose_name="Mijoz ismi")
    phone = models.CharField(max_length=25, verbose_name="Telefon raqami")
    active = models.BooleanField(default=False, verbose_name="Bog'lanib bo'lgandan keyin aktivlashtiring")

    class Meta:
        verbose_name = "📞 Mijoz arizasi"
        verbose_name_plural = "📞 Mijoz arizalari"