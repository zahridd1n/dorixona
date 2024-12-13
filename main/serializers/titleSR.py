from rest_framework import serializers
from main.models.titles import *
from main.serializers.functions import GeneralMixin

class BaseTitleSR(serializers.ModelSerializer, GeneralMixin):
    title = serializers.SerializerMethodField()
    subtitle = serializers.SerializerMethodField()

    class Meta:
        fields = ('title', 'subtitle')

    def get_title(self, obj):
        return self.get_translated_field(obj, 'title')

    def get_subtitle(self, obj):
        return self.get_translated_field(obj, 'subtitle')


class TitleAboutSR(BaseTitleSR):
    class Meta(BaseTitleSR.Meta):
        model = TitleAbout


class TitleProductSR(BaseTitleSR):
    class Meta(BaseTitleSR.Meta):
        model = TitleProduct


class TitleBlogSR(BaseTitleSR):
    class Meta(BaseTitleSR.Meta):
        model = TitleBlog


class TitleVideoSR(BaseTitleSR):
    class Meta(BaseTitleSR.Meta):
        model = TitleVideo


class TitleOffersSR(BaseTitleSR):
    class Meta(BaseTitleSR.Meta):
        model = TitleOffers


class TitleCommentsSR(BaseTitleSR):
    class Meta(BaseTitleSR.Meta):
        model = TitleComments


class TitleFaqSR(BaseTitleSR):
    image = serializers.ImageField()

    class Meta(BaseTitleSR.Meta):
        model = TitleFaq
        fields = BaseTitleSR.Meta.fields + ('image',)


class TitleBannerSR(BaseTitleSR):
    class Meta(BaseTitleSR.Meta):
        model = TitleBanner


class TitleContactSR(BaseTitleSR):
    class Meta(BaseTitleSR.Meta):
        model = TitleContact

class TitleProductDetailSR(BaseTitleSR):
    class Meta(BaseTitleSR.Meta):
        model = TitleProductDetail


