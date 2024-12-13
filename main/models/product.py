from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from colorfield.fields import ColorField
from django.utils.text import slugify
class ImageFon(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nomi")
    color = models.CharField(max_length=25, verbose_name="Rang")

    class Meta:
        verbose_name = "Fon rasmi"
        verbose_name_plural = "Fon rasmlari"

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name_uz = models.CharField(max_length=100, verbose_name="Maxsulot nomi (UZ)")
    name_ru = models.CharField(max_length=100, verbose_name="Maxsulot nomi (RU)")
    name_en = models.CharField(max_length=100, verbose_name="Maxsulot nomi (EN)")
    fields_uz = models.CharField(max_length=200, verbose_name="Xususiyatlari (UZ)")
    fields_ru = models.CharField(max_length=200, verbose_name="Xususiyatlari (RU)")
    fields_en = models.CharField(max_length=200, verbose_name="Xususiyatlari (EN)")
    detailmini_uz = models.TextField(verbose_name="Xususiyatlari (UZ)")
    detailmini_ru = models.TextField(verbose_name="Xususiyatlari (RU)")
    detailmini_en = models.TextField(verbose_name="Xususiyatlari (EN)")
    detail_uz = models.TextField(verbose_name="Mahsulot haqida uz tilida")
    detail_ru = models.TextField(verbose_name="Mahsulot haqida ru tilida")
    detail_en = models.TextField(verbose_name="Mahsulot haqida en tilida")
    content_uz = models.TextField(verbose_name="Mahsulot haqida uz tilida")
    content_ru = models.TextField(verbose_name="Mahsulot haqida ru tilida")
    content_en = models.TextField(verbose_name="Mahsulot haqida en tilida")
    description_uz = RichTextUploadingField(verbose_name="Mahsulot haqida batafsil uz tilida")
    description_ru = RichTextUploadingField(verbose_name="Mahsulot haqida batafsil ru tilida")
    description_en = RichTextUploadingField(verbose_name="Mahsulot haqida batafsil en tilida")
    slug = models.SlugField(unique=True, db_index=True,null=True,blank=True,verbose_name="Bu yerga hech nima yozilmasin ")
    active = models.BooleanField(default=False,verbose_name="Asosiy sahifada chiqishini hohlasangiz yoqing")
    background = models.ForeignKey(
        'ImageFon', on_delete=models.SET_NULL, null=True, verbose_name="Orqa fon"
    )
    image1 = models.ImageField(upload_to="product/image")
    image2 = models.ImageField(upload_to="product/image")
    image3 = models.ImageField(upload_to="product/image")
    image4 = models.ImageField(upload_to="product/image")

    def save(self, *args, **kwargs):
        if not self.slug and self.name_en:
            self.slug = slugify(self.name_en)  # name_en asosida slug yaratish
        super(Product, self).save(*args, **kwargs)  # Asl save metodini chaqirish

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"

    def __str__(self):
        return self.name_uz 
