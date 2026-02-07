from django.db import models


class Faq(models.Model):
    question_uz = models.CharField(max_length=200, verbose_name="Savol Matni uz tilida")
    question_ru = models.CharField(max_length=200, verbose_name="Savol Matni ru tilida")
    question_en = models.CharField(max_length=200, verbose_name="Savol Matni en tilida")
    answer_uz = models.CharField(max_length=200, verbose_name="Javob matni uz tilida")
    answer_ru = models.CharField(max_length=200, verbose_name="Javob matni ru tilida")
    answer_en = models.CharField(max_length=200, verbose_name="Javob matni en tilida")

    class Meta:
        verbose_name = "❓ FAQ — Savol-javob"
        verbose_name_plural = "❓ FAQ — Savol-javoblar"


class Comments(models.Model):
    name_uz = models.CharField(max_length=200, verbose_name="Mijoz ismi uz tilida")
    name_ru = models.CharField(max_length=200, verbose_name="Mijoz ismi ru tilida")
    comment_uz = models.TextField(verbose_name="Izoh matni uz tilida")
    comment_ru = models.TextField(verbose_name="Izoh matni ru tilida")
    comment_en = models.TextField(verbose_name="Izoh matni en tilida")
    additional_uz = models.CharField(max_length=200, verbose_name="Qo'shimcha uz tilida")
    additional_ru = models.CharField(max_length=200, verbose_name="Qo'shimcha ru tilida")
    additional_en = models.CharField(max_length=200, verbose_name="Qo'shimcha en tilida")
    image = models.ImageField(upload_to="comments/image")

    class Meta:
        verbose_name = "💬 Mijoz izohi"
        verbose_name_plural = "💬 Mijozlar izohlari"

    def __str__(self):
        return self.name_uz