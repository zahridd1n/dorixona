from rest_framework.response import Response
from rest_framework.views import APIView
from main.models.titles import *
from main.serializers.titleSR import *
from rest_framework import serializers
from main.function import custom_response

class Titles(APIView):
    def get(self, request, lang=None):
        context = {'lang': lang, 'request': request}
        # TitleAbout serializer
        title_about_serializer = TitleAboutSR(TitleAbout.objects.first(), context=context) if TitleAbout.objects.exists() else None
        # TitleProduct serializer
        title_product_serializer = TitleProductSR(TitleProduct.objects.first(), context=context) if TitleProduct.objects.exists() else None
        # TitleBlog serializer
        title_blog_serializer = TitleBlogSR(TitleBlog.objects.first(), context=context) if TitleBlog.objects.exists() else None
        # TitleVideo serializer
        title_video_serializer = TitleVideoSR(TitleVideo.objects.first(), context=context) if TitleVideo.objects.exists() else None
        # TitleOffers serializer
        title_offers_serializer = TitleOffersSR(TitleOffers.objects.first(), context=context) if TitleOffers.objects.exists() else None
        # TitleComments serializer
        title_comments_serializer = TitleCommentsSR(TitleComments.objects.first(), context=context) if TitleComments.objects.exists() else None
        # TitleFaq serializer (with image)
        title_faq_serializer = TitleFaqSR(TitleFaq.objects.first(), context=context) if TitleFaq.objects.exists() else None
        title_banner_serializer = TitleBannerSR(TitleBanner.objects.first(), context=context) if TitleBanner.objects.exists() else None
        # TitleContact serializer
        title_contact_serializer = TitleContactSR(TitleContact.objects.first(), context=context) if TitleContact.objects.exists() else None

        title_product_detail_serializer = TitleProductDetailSR(TitleProductDetail.objects.first(),context=context) if TitleProductDetail.objects.exists() else None

        # Return response with all data
        return custom_response({
           
            'about_title': title_about_serializer.data if title_about_serializer else None,
            'product_title': title_product_serializer.data if title_product_serializer else None,
            'blog_title': title_blog_serializer.data if title_blog_serializer else None,
            'video_title': title_video_serializer.data if title_video_serializer else None,
            'offers_title': title_offers_serializer.data if title_offers_serializer else None,
            'comments_title': title_comments_serializer.data if title_comments_serializer else None,
            'faq_title': title_faq_serializer.data if title_faq_serializer else None,
            'banner_title': title_banner_serializer.data if title_banner_serializer else None,
            'contact_title': title_contact_serializer.data if title_contact_serializer else None,
            'product_detail_title':title_product_detail_serializer.data if title_product_detail_serializer else None,
        
        })
