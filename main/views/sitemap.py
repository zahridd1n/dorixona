from main.models.product import Product
from main.models.blog_video import Blog
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.views import APIView
from django.utils import timezone



class SiteMap(APIView):
    def get(self, request):
        # Blog slug'larini olish
        blog_slugs = Blog.objects.values_list('slug', flat=True)
        
        # Service id'larini olish
        product_slug = Product.objects.values_list('slug', flat=True)
        
        # Til ro'yxati (bo'sh tilni qo'shamiz)
        langs = ['en', 'ru', '']
        
        # Bloglar uchun URL'larni yaratish
        blog_urls = [
            f"https://ghpharm.com/{lang}/blog/{slug}" 
            if lang else f"https://ghpharm.com/blog/{slug}" 
            for slug in blog_slugs
            for lang in langs
        ]
        
        # Service'lar uchun URL'larni yaratish
        service_urls = [
            f"https://ghpharm.com/{lang}/products/{service_id}" 
            if lang else f"https://ghpharm.com/services/{service_id}" 
            for service_id in product_slug
            for lang in langs
        ]
        
        domen = ['https://ghpharm.com/ru','https://ghpharm.com/en','https://ghpharm.com']

        statical_urls = []
        static_pages = ['about', 'products']  # Qo'shmoqchi bo'lgan statik sahifalar
        for page in static_pages:
            for lang in langs:
                if lang:
                    statical_urls.append(f"https://ghpharm.com/{lang}/{page}")
                else:
                    statical_urls.append(f"https://ghpharm.com/{page}")
        
        # Barcha URL'larni birlashtirish
        all_urls = domen + blog_urls + service_urls + statical_urls

        # XML faylni yaratish
        xml_content = self.generate_sitemap_xml(all_urls)
        
        # Javobni XML sifatida qaytarish
        return HttpResponse(xml_content, content_type='application/xml')

    def generate_sitemap_xml(self, urls):
        # XML bosh qismi
        xml = ['<?xml version="1.0" encoding="UTF-8"?>']
        xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

        # Har bir URL uchun XML element yaratish
        for url in urls:
            xml.append('<url>')
            xml.append(f'<loc>{url}</loc>')
            xml.append(f'<lastmod>{timezone.now().strftime("%Y-%m-%d")}</lastmod>')  # Oxirgi yangilanish sanasi
            xml.append('<changefreq>daily</changefreq>')  # O'zgarish tezligi
            xml.append('<priority>0.5</priority>')  # Prioritet
            xml.append('</url>')

        # XML oxirini yopish
        xml.append('</urlset>')

        # Barcha XML elementlarini birlashtirib qaytarish
        return '\n'.join(xml)
    

from django.http import FileResponse
import os

def robots_txt(request):
    # Fayl yo'lini aniqlash
    robots_file_path = os.path.join(os.path.dirname(__file__), 'robots.txt')

    # Faylni ochish va response sifatida yuborish
    try:
        return FileResponse(open(robots_file_path, 'rb'), content_type='text/plain')
    except FileNotFoundError:
        return HttpResponse("Fayl topilmadi", status=404)