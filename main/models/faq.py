from django.db import models


class Faq(models.Model):
    question_uz = models.CharField(max_length=200,verbose_name="Savol Matni uz tilida")
    question_ru = models.CharField(max_length=200,verbose_name="Savol Matni ru tilida")
    question_en = models.CharField(max_length=200,verbose_name="Savol Matni en tilida")
    answer_uz = models.CharField(max_length=200,verbose_name="Javob matni uz tilida")
    answer_ru = models.CharField(max_length=200,verbose_name="Javob matni ru tilida")
    answer_en = models.CharField(max_length=200,verbose_name="Javob matni en tilida")

    class Meta:
        verbose_name = "FAQ Savol va Javolari"
        verbose_name_plural = "FAQ Savol va Javolari"

        