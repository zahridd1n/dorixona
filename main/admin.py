from django.contrib import admin
from django.utils.html import format_html
from django.utils.text import slugify

from main.models.titles import (
    TitleAbout, TitleProduct, TitleBlog, TitleVideo, TitleOffers,
    TitleComments, TitleFaq, TitleBanner, TitleContact,
    TitleProductDetail, TitleHeader, AboutOfferTitle,
)
from main.models.offers import Offers, Offers2, About_offers3
from main.models.faq import Faq, Comments
from main.models.about import About, MiniAbout, Socials
from main.models.blog_video import Blog, Video, Footer, Client
from main.models.product import Product, ImageFon


admin.site.site_header = "🏥 Dorixona — Boshqaruv paneli"
admin.site.site_title = "Dorixona Admin"
admin.site.index_title = "Boshqaruv"


# ══════════════════════════════════════════════
# Mixins
# ══════════════════════════════════════════════

class LangTabMixin:
    uz_fields = ()
    ru_fields = ()
    en_fields = ()
    common_fields = ()

    def get_fieldsets(self, request, obj=None):
        fs = []
        if self.common_fields:
            fs.append(("⚙️ Umumiy", {"fields": self.common_fields}))
        if self.uz_fields:
            fs.append(("🇺🇿 O'zbekcha", {"fields": self.uz_fields, "classes": ("collapse",)}))
        if self.ru_fields:
            fs.append(("🇷🇺 Русский", {"fields": self.ru_fields, "classes": ("collapse",)}))
        if self.en_fields:
            fs.append(("🇬🇧 English", {"fields": self.en_fields, "classes": ("collapse",)}))
        return fs


class ImgMixin:
    def image_preview(self, obj):
        if hasattr(obj, 'image') and obj.image:
            return format_html('<img src="{}" height="50" style="border-radius:6px;"/>', obj.image.url)
        return "-"
    image_preview.short_description = "Rasm"

    def icon_preview(self, obj):
        if hasattr(obj, 'icon') and obj.icon:
            return format_html('<img src="{}" height="40"/>', obj.icon.url)
        return "-"
    icon_preview.short_description = "Icon"


# ══════════════════════════════════════════════
# 🏷 Sarlavhalar (BaseTitle)
# ══════════════════════════════════════════════

class BaseTitleAdmin(LangTabMixin, admin.ModelAdmin):
    uz_fields = ("title_uz", "subtitle_uz")
    ru_fields = ("title_ru", "subtitle_ru")
    en_fields = ("title_en", "subtitle_en")
    list_display = ("id", "title_uz", "subtitle_uz")
    search_fields = ("title_uz", "title_ru", "title_en")


@admin.register(TitleAbout)
class TitleAboutAdmin(BaseTitleAdmin):
    pass

@admin.register(TitleProduct)
class TitleProductAdmin(BaseTitleAdmin):
    pass

@admin.register(TitleBlog)
class TitleBlogAdmin(BaseTitleAdmin):
    pass

@admin.register(TitleVideo)
class TitleVideoAdmin(BaseTitleAdmin):
    pass

@admin.register(TitleOffers)
class TitleOffersAdmin(BaseTitleAdmin):
    pass

@admin.register(TitleComments)
class TitleCommentsAdmin(BaseTitleAdmin):
    pass

@admin.register(TitleFaq)
class TitleFaqAdmin(ImgMixin, BaseTitleAdmin):
    common_fields = ("image",)
    list_display = ("id", "title_uz", "image_preview")

@admin.register(TitleBanner)
class TitleBannerAdmin(BaseTitleAdmin):
    pass

@admin.register(TitleContact)
class TitleContactAdmin(BaseTitleAdmin):
    pass

@admin.register(TitleProductDetail)
class TitleProductDetailAdmin(BaseTitleAdmin):
    pass

@admin.register(TitleHeader)
class TitleHeaderAdmin(BaseTitleAdmin):
    pass

@admin.register(AboutOfferTitle)
class AboutOfferTitleAdmin(BaseTitleAdmin):
    pass


# ══════════════════════════════════════════════
# 🏢 Kompaniya haqida
# ══════════════════════════════════════════════

@admin.register(About)
class AboutAdmin(LangTabMixin, ImgMixin, admin.ModelAdmin):
    uz_fields = ("title_uz", "subtitle_uz", "mini_title_uz", "description_uz")
    ru_fields = ("title_ru", "subtitle_ru", "mini_title_ru", "description_ru")
    en_fields = ("title_en", "subtitle_en", "mini_title_en", "description_en")
    common_fields = ("image",)
    list_display = ("id", "title_uz", "mini_title_uz", "image_preview")
    search_fields = ("title_uz", "mini_title_uz")


@admin.register(MiniAbout)
class MiniAboutAdmin(LangTabMixin, ImgMixin, admin.ModelAdmin):
    uz_fields = ("title_uz", "subtitle_uz")
    ru_fields = ("title_ru", "subtitle_ru")
    en_fields = ("title_en", "subtitle_en")
    common_fields = ("image",)
    list_display = ("id", "title_uz", "image_preview")
    search_fields = ("title_uz",)


# ══════════════════════════════════════════════
# 🌐 Ijtimoiy tarmoqlar
# ══════════════════════════════════════════════

@admin.register(Socials)
class SocialsAdmin(ImgMixin, admin.ModelAdmin):
    list_display = ("id", "name", "link", "icon_preview")
    search_fields = ("name",)


# ══════════════════════════════════════════════
# 📝 Blog
# ══════════════════════════════════════════════

@admin.register(Blog)
class BlogAdmin(LangTabMixin, ImgMixin, admin.ModelAdmin):
    uz_fields = ("title_uz", "description_uz")
    ru_fields = ("title_ru", "description_ru")
    en_fields = ("title_en", "description_en")
    common_fields = ("image", "slug", "is_active")
    list_display = ("id", "title_uz", "is_active", "slug", "image_preview")
    list_filter = ("is_active",)
    list_editable = ("is_active",)
    search_fields = ("title_uz", "title_ru", "title_en")
    prepopulated_fields = {"slug": ("title_uz",)}

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.title_uz or "default-title")
        super().save_model(request, obj, form, change)


# ══════════════════════════════════════════════
# 🎬 Video
# ══════════════════════════════════════════════

@admin.register(Video)
class VideoAdmin(LangTabMixin, ImgMixin, admin.ModelAdmin):
    uz_fields = ("title_uz",)
    ru_fields = ("title_ru",)
    en_fields = ("title_en",)
    common_fields = ("image", "link", "is_active")
    list_display = ("id", "title_uz", "is_active", "video_link", "image_preview")
    list_filter = ("is_active",)
    list_editable = ("is_active",)

    def video_link(self, obj):
        if obj.link:
            return format_html('<a href="{}" target="_blank">▶ Ochish</a>', obj.link)
        return "-"
    video_link.short_description = "Video"


# ══════════════════════════════════════════════
# 🔻 Footer
# ══════════════════════════════════════════════

@admin.register(Footer)
class FooterAdmin(LangTabMixin, admin.ModelAdmin):
    uz_fields = ("title_uz", "subtitle_uz", "address_uz")
    ru_fields = ("title_ru", "subtitle_ru", "address_ru")
    en_fields = ("title_en", "subtitle_en", "address_en")
    common_fields = ("logo", "mini_text", "phone")
    list_display = ("id", "title_uz", "phone", "logo_preview")

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" height="40"/>', obj.logo.url)
        return "-"
    logo_preview.short_description = "Logo"


# ══════════════════════════════════════════════
# 📞 Mijoz arizalari
# ══════════════════════════════════════════════

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone", "active", "status_badge")
    list_filter = ("active",)
    list_editable = ("active",)
    search_fields = ("name", "phone")

    def status_badge(self, obj):
        if obj.active:
            return format_html('<span style="color:green;font-weight:bold;">✅ Bog\'lanildi</span>')
        return format_html('<span style="color:red;">⏳ Kutilmoqda</span>')
    status_badge.short_description = "Holat"


# ══════════════════════════════════════════════
# ❓ FAQ
# ══════════════════════════════════════════════

@admin.register(Faq)
class FaqAdmin(LangTabMixin, admin.ModelAdmin):
    uz_fields = ("question_uz", "answer_uz")
    ru_fields = ("question_ru", "answer_ru")
    en_fields = ("question_en", "answer_en")
    list_display = ("id", "question_uz", "short_answer")
    search_fields = ("question_uz", "question_ru", "question_en")

    def short_answer(self, obj):
        return obj.answer_uz[:80] + "..." if len(obj.answer_uz) > 80 else obj.answer_uz
    short_answer.short_description = "Javob"


# ══════════════════════════════════════════════
# 💬 Mijozlar izohi
# ══════════════════════════════════════════════

@admin.register(Comments)
class CommentsAdmin(LangTabMixin, ImgMixin, admin.ModelAdmin):
    uz_fields = ("name_uz", "comment_uz", "additional_uz")
    ru_fields = ("name_ru", "comment_ru", "additional_ru")
    en_fields = ("comment_en", "additional_en")
    common_fields = ("image",)
    list_display = ("id", "name_uz", "short_comment", "image_preview")
    search_fields = ("name_uz", "name_ru")

    def short_comment(self, obj):
        return obj.comment_uz[:100] + "..." if len(obj.comment_uz) > 100 else obj.comment_uz
    short_comment.short_description = "Izoh"


# ══════════════════════════════════════════════
# 🏆 Yutuqlar / Ustunliklar
# ══════════════════════════════════════════════

@admin.register(Offers)
class OffersAdmin(LangTabMixin, ImgMixin, admin.ModelAdmin):
    uz_fields = ("name_uz",)
    ru_fields = ("name_ru",)
    en_fields = ("name_en",)
    common_fields = ("total", "icon")
    list_display = ("id", "name_uz", "total", "icon_preview")
    search_fields = ("name_uz",)


@admin.register(Offers2)
class Offers2Admin(LangTabMixin, ImgMixin, admin.ModelAdmin):
    uz_fields = ("title_uz", "subtitle_uz")
    ru_fields = ("title_ru", "subtitle_ru")
    en_fields = ("title_en", "subtitle_en")
    common_fields = ("icon",)
    list_display = ("id", "title_uz", "subtitle_uz", "icon_preview")


@admin.register(About_offers3)
class AboutOffers3Admin(LangTabMixin, ImgMixin, admin.ModelAdmin):
    uz_fields = ("title_uz", "subtitle_uz")
    ru_fields = ("title_ru", "subtitle_ru")
    en_fields = ("title_en", "subtitle_en")
    common_fields = ("icon",)
    list_display = ("id", "title_uz", "subtitle_uz", "icon_preview")


# ══════════════════════════════════════════════
# 🎨 Fon rangi
# ══════════════════════════════════════════════

@admin.register(ImageFon)
class ImageFonAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "color", "color_box")

    def color_box(self, obj):
        return format_html(
            '<div style="width:40px;height:20px;background:{};border:1px solid #ccc;border-radius:4px;"></div>',
            obj.color
        )
    color_box.short_description = "Rang"


# ══════════════════════════════════════════════
# 💊 Mahsulotlar
# ══════════════════════════════════════════════

@admin.register(Product)
class ProductAdmin(LangTabMixin, admin.ModelAdmin):
    uz_fields = ("name_uz", "fields_uz", "detailmini_uz", "detail_uz", "content_uz", "description_uz")
    ru_fields = ("name_ru", "fields_ru", "detailmini_ru", "detail_ru", "content_ru", "description_ru")
    en_fields = ("name_en", "fields_en", "detailmini_en", "detail_en", "content_en", "description_en")
    common_fields = ("slug", "active", "background", "image1", "image2", "image3", "image4")
    list_display = ("id", "name_uz", "active", "slug", "bg_color", "img_preview")
    list_filter = ("active", "background")
    list_editable = ("active",)
    search_fields = ("name_uz", "name_ru", "name_en")
    prepopulated_fields = {"slug": ("name_en",)}

    def save_model(self, request, obj, form, change):
        if not obj.slug and obj.name_en:
            obj.slug = slugify(obj.name_en)
        super().save_model(request, obj, form, change)

    def bg_color(self, obj):
        if obj.background:
            return format_html(
                '<span style="padding:2px 10px;background:{};border-radius:4px;color:#fff;">{}</span>',
                obj.background.color, obj.background.name
            )
        return "-"
    bg_color.short_description = "Fon"

    def img_preview(self, obj):
        if obj.image1:
            return format_html('<img src="{}" height="50" style="border-radius:6px;"/>', obj.image1.url)
        return "-"
    img_preview.short_description = "Rasm"