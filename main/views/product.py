from rest_framework.response import Response
from rest_framework.views import APIView
from main.models.product import *
from main.models.titles import *

from main.serializers.productSR import *
from main.serializers.titleSR import *
from main.serializers.miniSR import *

from rest_framework import serializers
from rest_framework import status
from main.function import custom_response

class ProductView(APIView):
    """
    ProductView API view. Bu view foydalanuvchiga mahsulotlar haqidagi ma'lumotlarni beradi.
    Agar `slug` parametri yuborilsa, faqat shu `slug` bo'yicha mahsulotni chiqaradi, aks holda
    barcha mahsulotlarni ko'rsatadi. Shuningdek, tavsiya etilgan mahsulotlar ham ko'rsatiladi.
    """

    def get(self, request, lang=None):
        """
        GET so'rovi orqali mahsulotlar haqidagi ma'lumotlarni olish. 
        Agar `slug` parametri berilgan bo'lsa, faqat shu `slug` bo'yicha mahsulotni va tavsiya etilgan mahsulotlarni qaytaradi.
        Aks holda, barcha mahsulotlar ro'yxatini qaytaradi.
        """

        # Requestga moslang va til (lang) va so'rov (request) kontekstini yaratish
        context = {'lang': lang, 'request': request}

        # `slug` parametri so'rovda mavjud bo'lsa, uning qiymatini olish
        slug = request.query_params.get('slug', None)

        # Agar `slug` mavjud bo'lsa
        if slug:
            # `slug` bo'yicha mahsulotlarni olish
            products = Product.objects.filter(slug=slug)
            # Mahsulotlar mavjud bo'lsa
            if products.exists():
                # Topilgan mahsulotni serializerdan o'tkazish
                product_serializer = ProductSerializer(products, context=context, many=True)
                
                # Mahsulotga oid sarlavha (title) ma'lumotlarini olish
                product_title = TitleProductDetailSR(TitleProductDetail.objects.first(), context=context)

                # `slug` bo'yicha boshqa mahsulotlarni tavsiya etish (boshqa mahsulotlar)
                product_serializer_all = ProductSerializer(Product.objects.exclude(slug=slug), context=context, many=True)

                # Natijani qaytarish
                return Response({
                    'success': True,  # So'rov muvaffaqiyatli amalga oshdi
                    'message': 'Success',  # Xabar
                    'data': {  # Ma'lumotlar
                        'title': product_title.data,  # Mahsulotga oid sarlavha
                        'product': product_serializer.data,  # So'ralgan mahsulot
                        'recommended': product_serializer_all.data  # Tavsiya etilgan mahsulotlar
                    }
                })
            # Agar `slug` bo'yicha mahsulot topilmasa
            return Response({'success': False, 'message': 'No products found', 'data': {'product': None}}, status=status.HTTP_404_NOT_FOUND)

        # Agar `slug` yo'q bo'lsa, barcha mahsulotlarni olish
        product_serializer = ProductSerializer(Product.objects.all(), context=context, many=True)

        # Natijani qaytarish
        return custom_response({'product': product_serializer.data})
    

class HeaderView(APIView):
    def get(self, request, lang=None):
        context = {'lang': lang, 'request': request}
        product_serializer = ProductSerializer(Product.objects.filter(active=True), context=context, many=True)
        title_serializer = TitleHederSR(TitleHeader.objects.first(),context=context)
        offers_serializer = OffersSerializer(Offers.objects.all(),context=context,many=True)
        products = product_serializer.data
        filtered_products = [
            { 'slug': product.get('slug'), 'name': product.get('name'),'detailmini':product.get('detailmini'),
             'background':product.get('background'), 'images':product.get('images')}
            for product in products
        ]

        return custom_response({
            'title':title_serializer.data,
            'product': filtered_products,
            'offers':offers_serializer.data
        })