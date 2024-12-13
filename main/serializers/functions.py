class GeneralMixin:
    def get_translated_field(self, obj, field_name):  # Tilga asoslangan maydon qiymatini qaytaruvchi umumiy funksiya
        lang = self.context.get('lang')
        if lang == 'ru':
            return getattr(obj, f"{field_name}_ru")  # Masalan, title_ru qaytariladi
        elif lang == 'en':
            return getattr(obj, f"{field_name}_en")  # Masalan, title_en qaytariladi
        else:
            return getattr(obj, f"{field_name}_uz")  # Masalan, title_uz qaytariladi


