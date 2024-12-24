from rest_framework import serializers
from main.models.product import Product
from main.serializers.functions import GeneralMixin

class ProductSerializer(serializers.ModelSerializer, GeneralMixin):
    name = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    detailmini = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()  # Barcha rasmlar uchun yangi field
    class Meta:
        model = Product
        fields = ('slug','name', 'detail', 'content', 'description', 'detailmini', 'background','images',)
        depth = 1

    def get_name(self, obj):
        return self.get_translated_field(obj, 'name')

    def get_detailmini(self, obj):
        return self._get_translated_list(obj, 'detailmini')

    def get_detail(self, obj):
        return self._get_translated_dict(obj, 'detail')

    def get_content(self, obj):
        return self._get_translated_dict(obj, 'content')

    def get_description(self, obj):
        return self.get_translated_field(obj, 'description')

    def get_images(self, obj):
        """Barcha rasmlarni ro'yxat shaklida qaytaradi."""
        request = self.context.get('request')  # Request ob'ektini kontekstdan olish
        if not request:
            return None  # Request mavjud bo'lmasa, bo'sh qiymat qaytariladi
        
        images = [obj.image1.url, obj.image2.url, obj.image3.url, obj.image4.url]
        host = f"{request.scheme}://{request.get_host()}"  # Host va protokolni aniqlash
        return [f"{host}{img}" for img in images if img] # Faqat mavjud bo'lgan rasmlar
    # Yordamchi metodlar
    def _get_translated_list(self, obj, field_name):
        """Bo'sh joylar bilan ajratilgan so'zlar ro'yxatini qaytaradi."""
        field_value = self.get_translated_field(obj, field_name)
        return [item.strip() for item in field_value.split(",")]

    def _get_translated_dict(self, obj, field_name):
        """'key=value' formatida bo'lgan qiymatlarni ajratib, lug'at shaklida qaytaradi."""
        field_value = self.get_translated_field(obj, field_name)
        result = []
        for line in field_value.split("\r\n"):
            if "=" in line:
                key, value = line.split("=", 1)
                result.append([key.strip(), value.strip()])
        return result
