from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from main.models.titles import BaseTitle,BaseMetaMixin

class Offers(models.Model):
    name_uz = models.CharField(max_length=100, verbose_name="Nomlanishi uz tilida")
    name_ru = models.CharField(max_length=100, verbose_name="Nomlanishi ru tilida")
    name_en = models.CharField(max_length=100, verbose_name="Nomlanishi en tilida")
    total = models.IntegerField(verbose_name="Raqamlarda kiriting", validators=[MinValueValidator(1), MaxValueValidator(99999)])
    icon = models.ImageField(upload_to="offers/icon", verbose_name="icon biriktiring")  # Nisbiy yo'l

    class Meta:
        verbose_name = "Yutuqlarimiz"
        verbose_name_plural = "Yutuqlarimiz"


class Offers2(BaseTitle):
    icon = models.ImageField(upload_to="offers/icon", verbose_name="Icon biriktiring")  # Nisbiy yo'l

    class Meta:
        verbose_name = "Yutuqlarimiz2"
        verbose_name_plural = "Yutuqlarimiz2"


class About_offers3(BaseTitle):
      # Offers2 ni meros qilib olishdan saqlanish
    icon = models.ImageField(upload_to="offers/icon", verbose_name="Icon biriktiring")  # Nisbiy yo'l

    class Meta:
        verbose_name = "About sahifasi uchun offers11"
        verbose_name_plural = "About sahifasi uchun offers11"
    