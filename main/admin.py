from django.contrib import admin
from main.models.titles import *
from main.models.offers import *
from main.models.faq import *
from main.models.product import *


from django.apps import apps

# Modellar ro'yxatini olish
models = apps.get_models()

# Ro'yxatni qayta tekshirib chiqamiz va faqat bir marta ro'yxatdan o'tkazish uchun
for model in models:
    # Titles va Offers modellarini tekshirish
    if model.__module__ in ["main.models.titles", "main.models.offers","main.models.faq","main.models.product"]:
        # Dinamik admin klassi yaratish
        class DynamicAdmin(admin.ModelAdmin):
            list_display = [field.name for field in model._meta.fields]  # Barcha maydonlarni chiqarish

        # Admin saytga modelni ro'yxatdan o'tkazish (faqat bir marta)
        if not admin.site.is_registered(model):
            admin.site.register(model, DynamicAdmin)


