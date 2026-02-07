from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from main.models.titles import BaseTitle


class Offers(models.Model):
    name_uz = models.CharField(max_length=100, verbose_name="Nomlanishi uz tilida")
    name_ru = models.CharField(max_length=100, verbose_name="Nomlanishi ru tilida")
    name_en = models.CharField(max_length=100, verbose_name="Nomlanishi en tilida")
    total = models.IntegerField(verbose_name="Raqamlarda kiriting", validators=[MinValueValidator(1), MaxValueValidator(99999)])
    icon = models.ImageField(upload_to="offers/icon", verbose_name="icon biriktiring")

    class Meta:
        verbose_name = "🏆 Yutuq — raqamlarda"
        verbose_name_plural = "🏆 Yutuqlar — raqamlarda"


class Offers2(BaseTitle):
    icon = models.ImageField(upload_to="offers/icon", verbose_name="Icon biriktiring")

    class Meta:
        verbose_name = "🏆 Yutuq — ustunlik"
        verbose_name_plural = "🏆 Yutuqlar — ustunliklar"


class About_offers3(BaseTitle):
    icon = models.ImageField(upload_to="offers/icon", verbose_name="Icon biriktiring")

    class Meta:
        verbose_name = "🏆 Haqimizda — ustunlik"
        verbose_name_plural = "🏆 Haqimizda — ustunliklar"