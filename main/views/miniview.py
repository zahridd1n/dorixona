from rest_framework.response import Response
from rest_framework.views import APIView
from main.models.product import *
from main.models.titles import *
from main.models.faq import *
from main.serializers.miniSR import *
from main.serializers.aboutSR import *
from main.serializers.titleSR import *



class MiniView(APIView):
    def get(self, request, lang=None):
        context = {'lang': lang, 'request': request}

        # Serializerni yaratishda 'many=True' faqat serializer darajasida bo'lishi kerak
        faq_serializer = FaqSerializer(Faq.objects.all(), context=context, many=True)
        comment_serializer = CommentSerializer(Comments.objects.all(), context=context, many=True)  # 'many=True' to'g'ri ishlatilgan
        offers_serializer = OffersSerializer2(Offers2.objects.all().order_by('id'), context=context, many=True)

        # Responseni qaytarish
        return Response({
            'success': True,
            'message': 'Success',
            'data': {
                'faq': faq_serializer.data,
                'comments': comment_serializer.data,
                'offers': offers_serializer.data
            }
        })


