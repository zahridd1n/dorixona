from main.models.offers import *
from main.models.faq import *

from main.serializers.functions import GeneralMixin
from rest_framework import serializers
from main.serializers.titleSR import BaseTitleSR

class OffersSerializer(serializers.ModelSerializer,GeneralMixin):
    name = serializers.SerializerMethodField()
    
    class Meta:
        model = Offers
        fields = ('name','total','icon')

    def get_name(self,obj):
        return self.get_translated_field(obj,'name')
    
class OffersSerializer2(BaseTitleSR):
    class Meta(BaseTitleSR.Meta):
        model = Offers2
        fields = BaseTitleSR.Meta.fields + ('icon',)


class About_Offers_Serializer(BaseTitleSR):
    class Meta(BaseTitleSR.Meta):
        model = About_offers
        fields = BaseTitleSR.Meta.fields + ('icon',)


class FaqSerializer(serializers.Serializer, GeneralMixin):
    question = serializers.SerializerMethodField()
    answer = serializers.SerializerMethodField()

    class Meta:
        model = Faq
        fields = ('question', 'answer')

    def get_question(self, obj):
        return self.get_translated_field(obj, 'question')

    def get_answer(self, obj):
        return self.get_translated_field(obj, 'answer')
    


class CommentSerializer(serializers.ModelSerializer, GeneralMixin):
    name = serializers.SerializerMethodField()
    comment = serializers.SerializerMethodField()
    additional = serializers.SerializerMethodField()

    class Meta:
        model = Comments
        fields = ('name', 'comment', 'additional', 'image')  # Ensure 'image' is a valid field on the model

    def get_name(self, obj):
        return self.get_translated_field(obj, 'name')  # Assuming get_translated_field is defined in your GeneralMixin

    def get_comment(self, obj):
        return self.get_translated_field(obj, 'comment')

    def get_additional(self, obj):
        return self.get_translated_field(obj, 'additional')
    
