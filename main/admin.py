from django.contrib import admin
from main.models.candidates import Candidate, Skill

# Skill modelini ro'yxatga olish
admin.site.register(Skill)

# Candidate modelini ro'yxatga olish
class CandidateAdmin(admin.ModelAdmin):
    # Ko'rsatiladigan ustunlar
    list_display = ('name', 'date_of_birth', 'expected_salary', 'phone_number', 'tg_username')
    # Qidiruvni faollashtirish
    search_fields = ('name', 'phone_number', 'tg_username')
    # Filtrlar qo'shish


    # Ko'rsatilgan ko'rsatmalarni o'zgartirish
    fieldsets = (
        (None, {
            'fields': ('name', 'date_of_birth', 'address', 'experience', 'experience_name', 'expected_salary')
        }),
        ('Aloqa', {
            'fields': ('phone_number', 'tg_username')
        }),
        ("Batafsil ma'lumot", {
            'fields': ('description',)
        })
    )

    # Ko'nikmalarni ko'rsatish va tahrirlash uchun maxsus konfiguratsiya

# Candidate modelini admin panelga ro'yxatga olish
admin.site.register(Candidate, CandidateAdmin)
