from rest_framework.response import Response
from rest_framework.views import APIView
from main.models.product import *
from main.models.titles import *
from main.models.faq import *
from main.serializers.miniSR import *
from main.serializers.aboutSR import *
from main.serializers.titleSR import *
from main.function import custom_response
from main.models.blog_video import Client
import urllib.parse
from config.settings import BOT_TOKEN,GROUP_ID
import requests
class MiniView(APIView):
    """
    MiniView bu API view bo'lib, `GET` sorovi bilan foydalanuvchiga
    FAQ (savol-javob), comments (izohlar) va offers (takliflar) ma'lumotlarini 
    bir vaqtning o'zida taqdim etadi.
    """

    def get(self, request, lang=None):
        # Foydalanuvchidan kelgan so'rovga mos lang (til) va request kontekstini yaratish
        context = {'lang': lang, 'request': request}

        # Faq (savol-javoblar) ro'yxatini olish va serializatsiya qilish
        faq_serializer = FaqSerializer(Faq.objects.all(), context=context, many=True)

        # Comments (izohlar) ro'yxatini olish va serializatsiya qilish
        comment_serializer = CommentSerializer(Comments.objects.all(), context=context, many=True)

        # Offers (takliflar) ro'yxatini olish va serializatsiya qilish
        offers_serializer = OffersSerializer2(Offers2.objects.all().order_by('id'), context=context, many=True)

        # Barcha serializatsiya qilingan ma'lumotlarni custom_response yordamida qaytarish
        return custom_response({
            'faq': faq_serializer.data,  # FAQ ma'lumotlari
            'comments': comment_serializer.data,  # Izohlar
            'offers': offers_serializer.data  # Takliflar
        })


class SendMSG(APIView):
    def post(self, request, lang, name, phone):
        # POST so'rovini to'g'ri tarzda olish
        name = name
        phone = phone

        if name and phone:
            # Mijozni yaratish
            Client.objects.create(name=name, phone=phone)

            # Xabar matni
            text = f"Saytdan Xabar:\nMijoz Konsultatsiya olmoqchi\n👤 Mijoz ismi: {name}\n📞 Telefon: {phone}"
            encoded_text = urllib.parse.quote_plus(text)

            # Telegram bot orqali xabar yuborish
            url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={GROUP_ID}&text={encoded_text}'
            requests.get(url)

            # Tilga qarab javob
            messages = {
                "uz": "Sizning so'rovingiz muvaffaqiyatli yuborildi",
                "ru": "Xabaringiz yuborildi ruscha matn",
                "en": "Inglizcha matn",
            }

            return Response({
                'status': True,
                'message': messages.get(lang, "Xabar yuborildi")
            })

        # Agar 'name' yoki 'phone' bo'lmasa
        messages = {
            "uz": "Malumotlarni to'g'ri kiriting",
            "ru": "Xabaringiz yuborildi ruscha matn",
            "en": "Inglizcha matn",
        }
        return Response({
            'status': False,
            'message': messages.get(lang, "Xabar yuborilmadi")
        })

