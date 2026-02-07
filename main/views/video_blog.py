from rest_framework.response import Response
from rest_framework.views import APIView
from main.models.blog_video import *
from main.serializers.blogvideoSR import *
from main.function import custom_response

class GetVideo(APIView):
    """
    GetVideo - bu video va blog ma'lumotlarini olish uchun ishlatiladigan APIView.
    Ushbu API faqat GET so'rovlarini qabul qiladi va faqat asosiy sahifa uchun faol (is_active=True) videolar hamda bloglar haqidagi ma'lumotlarni qaytaradi.
    """

    def get(self, request, lang=None):
        """
        GET so'rovini qayta ishlash uchun metod.

        Bu metod video va blog ma'lumotlarini qaytaradi:
        - Faol bo'lgan videolar (is_active=True) faqat asosiy sahifada ko'rsatiladigan.
        - Faol bo'lgan bloglar (is_active=True) faqat asosiy sahifada ko'rsatiladigan.
        """

        # Kontextni sozlash (til va so'rov uchun)
        context = {'lang': lang, 'request': request}

        # Faol videolarni olish va serializer qilish (faqat asosiy sahifa uchun)
        videoserializer = VideoSerializer(Video.objects.filter(is_active=True), context=context, many=True)

        # Faol bloglarni olish va serializer qilish (faqat asosiy sahifa uchun)
        blogserializer = BlogSerializer(Blog.objects.filter(is_active=True), context=context, many=True)

        # Natijalarni qaytarish
        return custom_response({
            'videos': videoserializer.data,  # Faol videolar (faqat asosiy sahifa)
            'blogs': blogserializer.data,    # Faol bloglar (faqat asosiy sahifa)
        })

    
class GetBlog(APIView):
    """
    GetBlog - bu blog sahifasiga oid ma'lumotlarni olish uchun ishlatiladigan APIView.
    Ushbu API faqat GET so'rovlarini qabul qiladi va blog maqolalari haqidagi ma'lumotlarni qaytaradi.
    
    - Agar so'rovda slug parametri yuborilsa, ma'lum slug bilan bog'liq bo'lgan blogni va unga tegishli tavsiya qilingan bloglarni qaytaradi.
    - Agar slug parametri yuborilmasa, bazadagi birinchi blogni va unga tegishli tavsiya qilingan bloglarni qaytaradi.
    """

    def get(self, request, lang=None):
        """
        GET so'rovini qayta ishlash uchun metod.

        Bu metod blog sahifasini qaytaradi, unda:
        - Agar slug parametrini yuborilsa, slugga mos keladigan blog va tavsiya qilingan bloglar.
        - Agar slug berilmasa, birinchi blog va tavsiya qilingan bloglar.
        """

        # Kontextni sozlash (til va so'rov uchun)
        context = {'lang': lang, 'request': request}
        
        # URL parametridan slug olish (agar mavjud bo'lsa)
        slug = request.query_params.get('slug', None)
        
        if slug:
            # Slug bo'yicha topilgan blogni olish
            blog = Blog.objects.filter(slug=slug).first()
            blogserializer = BlogSerializer(blog, context=context)

            # Slug bilan topilgan blogni chiqarib tashlash
            recomended = Blog.objects.exclude(slug=slug)
            recomended_serializer = BlogSerializer(recomended, context=context, many=True)
        else:
            # Agar slug mavjud bo'lmasa, birinchi blogni olish
            blog = Blog.objects.all().first()
            blogserializer = BlogSerializer(blog, context=context)

            # Hammasidan slugni chiqarib tashlash
            recomended = Blog.objects.exclude(slug=blog.slug)
            recomended_serializer = BlogSerializer(recomended, context=context, many=True)
        
        return custom_response({
            'blog': blogserializer.data,  # Topilgan blog
            'recomended': recomended_serializer.data 
            })
        
    

class FooterView(APIView):
    def get(self,request,lang=None):
        context = {'lang': lang, 'request': request}

        footsr= FooterSerializer(Footer.objects.first(),context=context)

        return custom_response({
            'footer':footsr.data
        })

        