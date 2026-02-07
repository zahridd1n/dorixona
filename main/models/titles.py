from django.db import models


class BaseTitle(models.Model):
    title_uz = models.CharField(max_length=100, verbose_name="Kichik Sarlavha uzbek tilida")
    title_ru = models.CharField(max_length=100, verbose_name="Kichik Sarlavha rus tilida")
    title_en = models.CharField(max_length=100, verbose_name="Kichik Sarlavha ingliz tilida")
    subtitle_uz = models.CharField(max_length=100, verbose_name="Sarlavha uzbek tilida")
    subtitle_ru = models.CharField(max_length=100, verbose_name="Sarlavha rus tilida")
    subtitle_en = models.CharField(max_length=100, verbose_name="Sarlavha ingliz tilida")

    class Meta:
        abstract = True


class TitleAbout(BaseTitle):
    class Meta:
        verbose_name = "🏷 Sarlavha — Biz haqimizda"
        verbose_name_plural = "🏷 Sarlavha — Biz haqimizda"


class TitleProduct(BaseTitle):
    class Meta:
        verbose_name = "🏷 Sarlavha — Mahsulotlar"
        verbose_name_plural = "🏷 Sarlavha — Mahsulotlar"


class TitleBlog(BaseTitle):
    class Meta:
        verbose_name = "🏷 Sarlavha — Maqolalar"
        verbose_name_plural = "🏷 Sarlavha — Maqolalar"


class TitleVideo(BaseTitle):
    class Meta:
        verbose_name = "🏷 Sarlavha — Videolar"
        verbose_name_plural = "🏷 Sarlavha — Videolar"


class TitleOffers(BaseTitle):
    class Meta:
        verbose_name = "🏷 Sarlavha — Ustunligimiz"
        verbose_name_plural = "🏷 Sarlavha — Ustunligimiz"


class TitleComments(BaseTitle):
    class Meta:
        verbose_name = "🏷 Sarlavha — Mijozlar fikri"
        verbose_name_plural = "🏷 Sarlavha — Mijozlar fikri"


class TitleFaq(BaseTitle):
    image = models.ImageField(upload_to="faq/icons", verbose_name="FAQ icon")

    class Meta:
        verbose_name = "🏷 Sarlavha — FAQ"
        verbose_name_plural = "🏷 Sarlavha — FAQ"


class TitleBanner(BaseTitle):
    class Meta:
        verbose_name = "🏷 Sarlavha — Banner"
        verbose_name_plural = "🏷 Sarlavha — Banner"


class TitleContact(BaseTitle):
    class Meta:
        verbose_name = "🏷 Sarlavha — Kontakt"
        verbose_name_plural = "🏷 Sarlavha — Kontakt"


class TitleProductDetail(BaseTitle):
    class Meta:
        verbose_name = "🏷 Sarlavha — Mahsulot sahifasi"
        verbose_name_plural = "🏷 Sarlavha — Mahsulot sahifasi"


class TitleHeader(BaseTitle):
    class Meta:
        verbose_name = "🏷 Sarlavha — Bosh sahifa"
        verbose_name_plural = "🏷 Sarlavha — Bosh sahifa"


class AboutOfferTitle(BaseTitle):
    class Meta:
        verbose_name = "🏷 Sarlavha — Haqimizda ustunlik"
        verbose_name_plural = "🏷 Sarlavha — Haqimizda ustunlik"