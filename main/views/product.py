from rest_framework.response import Response
from rest_framework.views import APIView
from main.models.product import *
from main.serializers.productSR import *
from rest_framework import serializers
from rest_framework import status



class ProductView(APIView):
    def get(self, request, lang=None):
        context = {'lang': lang, 'request': request}
        product_serialier = ProductSerializer(Product.objects.all(),context=context,many=True) if Product.objects.exists() else None

        return Response({
            'success': True,
            'message': 'Success',
            'data': {
                'product': product_serialier.data if product_serialier else None,
            }
        })
