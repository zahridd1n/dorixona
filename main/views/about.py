from rest_framework.response import Response
from rest_framework.views import APIView
from main.models.about import *
from main.models.titles import *
from rest_framework import status
from main.serializers.aboutSR import *
from main.serializers.miniSR import *
from main.serializers.titleSR import *
from main.function import custom_response

from rest_framework import serializers



class AboutView(APIView):
    def get(self, request, lang=None):
        # Lang va request parametrlarini contextga qo'shamiz
        context = {'lang': lang, 'request': request}

        # About obyektining birinchi yozuvini serializerlaymiz
        about_object = About.objects.first()  # About modelidan birinchi obyektni olish
        if not about_object:  # Agar bo'sh bo'lsa
            return Response({
                'success': False,
                'message': 'About object not found.',
            }, status=status.HTTP_404_NOT_FOUND)
        
        # Serializerlarni yaratish
        about_serializer = AboutSerializer(about_object, context=context)
        about_offer_serializer = About_Offers_Serializer(About_offers1.objects.all(), context=context, many=True)
        mini_about_serializer = MiniAboutSerializer(MiniAbout.objects.all(), context=context, many=True)
        about_title_serializer = AboutOfferTitleSR(AboutOfferTitle.objects.first(), context=context)

        # Natijani qaytarish
        return custom_response({
            'about': about_serializer.data,
            'mini_about': mini_about_serializer.data,
            'title': about_title_serializer.data,
            'offers_about': about_offer_serializer.data,
            
        })