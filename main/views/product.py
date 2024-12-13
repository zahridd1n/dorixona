from rest_framework.response import Response
from rest_framework.views import APIView
from main.models.product import *
from main.models.titles import *

from main.serializers.productSR import *
from main.serializers.titleSR import *
from main.serializers.miniSR import *

from rest_framework import serializers
from rest_framework import status


class ProductView(APIView):
    def get(self, request, lang=None):
        context = {'lang': lang, 'request': request}
        slug = request.query_params.get('slug', None)

        if slug:
            products = Product.objects.filter(slug=slug)
            if products.exists():
                product_serializer = ProductSerializer(products, context=context, many=True)
                product_title = TitleProductDetailSR(TitleProductDetail.objects.first(), context=context)
                product_serializer_all = ProductSerializer(Product.objects.exclude(slug=slug), context=context, many=True)

                return Response({
                    'success': True,
                    'message': 'Success',
                    'data': {'title': product_title.data,'product': product_serializer.data,'recommended':product_serializer_all.data}
                })
            return Response({'success': False, 'message': 'No products found', 'data': {'product': None}}, status=status.HTTP_404_NOT_FOUND)

        product_serializer = ProductSerializer(Product.objects.all(), context=context, many=True)
        return Response({'success': True, 'message': 'Success', 'data': {'product': product_serializer.data}})
    

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

        return Response({
            'success': True,
            'message': 'Success',
            'data': {
                'title':title_serializer.data,
                'product': filtered_products,
                'offers':offers_serializer.data
               
            }
        })