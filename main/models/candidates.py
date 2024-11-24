from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=50, verbose_name="Skill nomlari")

    def __str__(self):
        return self.name


class Candidate(models.Model):
    STATUS_CHOICES = [
        ('yangi', 'yangi'),
        ('jarayonda', 'jarayonda'),
        ('intervyu_rejalashtirilgan', 'intervyu_rejalashtirilgan'),
        ('intervyu_qilingan', 'intervyu_qilingan'),
        ('taklif_berilgan', 'taklif_berilgan'),
        ('qabul_qilingan', 'qabul_qilingan'),
        ('rad_etilgan', 'rad_etilgan'),
        ('kutish', 'kutish'),
    ]
    name = models.CharField(max_length=200, verbose_name="Nomzod ismi")
    date_of_birth = models.DateField(verbose_name="Tug'ilgan sanasi")
    address = models.CharField(max_length=500, verbose_name="Nomzod Manzili")
    experience = models.CharField(max_length=500, verbose_name="Tajriba yili")
    experience_name = models.CharField(max_length=600, verbose_name="Qaysi sohalarda ishlagani")
    skill=models.CharField(max_length=500, verbose_name="Ko'nikmalar")
    expected_salary = models.CharField(max_length=600, verbose_name="Kutilayotgan oylik maosh miqdori (so‘m)")
    phone_number = models.CharField(max_length=20, verbose_name="Nomzod telefon raqami")
    tg_username = models.CharField(max_length=50, verbose_name="Nomzod telegram username")
    description = models.TextField(verbose_name="Nomzod ozi haqida batafsil")
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=200,
        choices=STATUS_CHOICES,
        default='yangi'
    )

    def __str__(self):
        return self.name
