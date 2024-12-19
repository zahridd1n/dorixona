from django.contrib import admin
from main.models.titles import *
from main.models.offers import *
from main.models.faq import *
from main.models.product import *
from main.models.blog_video import *

from django.utils.text import slugify

from django.apps import apps

# Modellar ro'yxatini olish
models = apps.get_models()

# Ro'yxatni qayta tekshirib chiqamiz va faqat bir marta ro'yxatdan o'tkazish uchun
for model in models:
    # Titles va Offers modellarini tekshirish
    if model.__module__ in ["main.models.titles", "main.models.offers", "main.models.faq", "main.models.product","main.models.about","main.models.blog_video", "main.models.blog"]:
        # Dinamik admin klassi yaratish
        class DynamicAdmin(admin.ModelAdmin):
            list_display = [field.name for field in model._meta.fields]  # Barcha maydonlarni chiqarish

            # save_model metodini o'zgartirish
            def save_model(self, request, obj, form, change):
                if isinstance(obj, Product) and not obj.slug:  # faqat Product modeli uchun
                    obj.slug = slugify(obj.name_en)  # name_en dan slug yaratish
                elif isinstance(obj, Blog) and not obj.slug:  # faqat Blog modeli uchun
                    obj.slug = slugify(obj.title_uz)  # title_uz dan slug yaratish
                super().save_model(request, obj, form, change)  # Asl save_model ni chaqirish

        # Admin saytga modelni ro'yxatdan o'tkazish (faqat bir marta)
        if not admin.site.is_registered(model):
            admin.site.register(model, DynamicAdmin)

