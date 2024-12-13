from rest_framework import serializers
from main.models.product import Product
from main.serializers.functions import GeneralMixin

# class ProductSerializer(serializers.ModelSerializer, GeneralMixin):
#     name = serializers.SerializerMethodField()
#     detail = serializers.SerializerMethodField()


#     class Meta:
#         model = Product
#         fields = ('name_uz', 'fields_uz', 'detail_uz', 'content_uz', 'description_uz', )

#     def get_name(self, obj):
#         return self.get_translated_field(obj, 'name')


#     def get_fields(self, obj):
#         return self.get_translated_field(obj, 'fields')

#     def get_detail(self, obj):
#         return self.get_translated_field(obj, 'detail')



class ProductSerializer(serializers.ModelSerializer, GeneralMixin):
    name = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    # fields = serializers.SerializerMethodField()
    detailmini = serializers.SerializerMethodField()



    class Meta:
        model = Product
        fields = ('name','detail','content','description','detailmini','image1', 'image2', 'image3', 'image4')

    def get_name(self, obj):
        return self.get_translated_field(obj, 'name')
    def get_detailmini(self, obj):
        
        detailmini = self.get_translated_field(obj, 'detailmini')
        result = []

        for item in detailmini.split(","):
            result.append(item.strip())
        return result

    def get_detail(self, obj):
        detail = self.get_translated_field(obj, 'detail')  # Detailni olish
        
        detail_lines = detail.split("\r\n")  # Yangi qatorlar bo'yicha ajratish
        
        # 'key=value' formatidagi qiymatlarni ajratish
        result = []
        for line in detail_lines:
            if "=" in line:
                key, value = line.split("=", 1)  # '=' bo'yicha ajratish
                result.append([key.strip(), value.strip()])  # Bo'sh joylarni olib tashlash
        
        return result  # Natijani qaytarish
    
    def get_content(self, obj):
        content =  self.get_translated_field(obj, 'content')

        content_lines = content.split("\r\n")
        result = []
        for line in content_lines:
            if "=" in line:
                key,value=line.split("=",1)
                result.append([key.strip(),value.strip()])
        return result

    

    def get_description(self, obj):
        return self.get_translated_field(obj, 'description')