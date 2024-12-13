from main.models.about import *
from main.serializers.functions import GeneralMixin
from rest_framework import serializers
from main.serializers.titleSR import BaseTitleSR


class AboutSerializer(serializers.Serializer,GeneralMixin):
    title = serializers.SerializerMethodField()
    subtitle = serializers.SerializerMethodField()
    mini_title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    class Meta:
        model = About
        fields = ('image','title','subtile','mini_title','description',)

    def get_title(self,obj):
            return self.get_translated_field(obj,'title')
    
    def get_subtitle(self,obj):
            return self.get_translated_field(obj,'subtitle')
    
    def get_mini_title(self,obj):
            return self.get_translated_field(obj,'mini_title')
    
    def get_description(self,obj):
            return self.get_translated_field(obj,'description')
    
    def get_image(self, obj):
        # Rasmga to'liq URL qo'shish
        request = self.context.get('request')
        image_url = obj.image.url  # Rasmning URL yo'li
        if request is not None:
            return request.build_absolute_uri(image_url)
        return image_url
    
class MiniAboutSerializer(AboutSerializer):
    def get_mini_title(self, obj):
        return None  # Bo'sh qiymat qaytarish

    def get_description(self,obj):
        return None
    class Meta:
        fields = ('title', 'subtitle', 'image')


        
