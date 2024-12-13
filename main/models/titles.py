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


class BaseMetaMixin:
    """Avtomatik verbose_name va verbose_name_plural yaratish."""
    @classmethod
    def generate_meta(cls, name):
        class Meta:
            verbose_name = f"Sarlavha {name}"
            verbose_name_plural = f"Sarlavha {name}"
        return Meta


class TitleAbout(BaseTitle):
    class Meta(BaseMetaMixin.generate_meta("Haqimizda")):
        pass


class TitleProduct(BaseTitle):
    class Meta(BaseMetaMixin.generate_meta("Mahsulotlar")):
        pass


class TitleBlog(BaseTitle):
    class Meta(BaseMetaMixin.generate_meta("Maqolalar")):
        pass


class TitleVideo(BaseTitle):
    class Meta(BaseMetaMixin.generate_meta("Videolar")):
        pass

class TitleOffers(BaseTitle):
    class Meta(BaseMetaMixin.generate_meta("Ustunligimiz")):
        pass

class TitleComments(BaseTitle):
    class Meta(BaseMetaMixin.generate_meta("Mijozlar fikri")):
        pass

class TitleFaq(BaseTitle):
    image = models.ImageField(upload_to="faq/icons", verbose_name="FAQ icon")  # Rasm qo'shish

    class Meta(BaseMetaMixin.generate_meta("FAQ")):
        pass

class TitleBanner(BaseTitle):
    class Meta(BaseMetaMixin.generate_meta("Banner")):
        pass

class TitleContact(BaseTitle):
    class Meta(BaseMetaMixin.generate_meta("Kontakt")):
        pass

class TitleProductDetail(BaseTitle):
    class Meta(BaseMetaMixin.generate_meta("Product detail sahifasi")):
        pass
