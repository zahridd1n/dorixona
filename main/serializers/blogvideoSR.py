from main.models.blog_video import Blog,Footer,Video,Client
from main.serializers.functions import GeneralMixin
from rest_framework.serializers import ModelSerializer,SerializerMethodField
from main.serializers.titleSR import BaseTitleSR

class VideoSerializer(ModelSerializer,GeneralMixin):
    title = SerializerMethodField()

    class Meta:
        model = Video
        fields = ('title','link','image','is_active',)

    def get_title(self,obj):
        return self.get_translated_field(obj,'title')
    
class FooterSerializer(BaseTitleSR):
    address = SerializerMethodField()

    class Meta:
        model = Footer
        fields = ('title', 'subtitle', 'address', 'phone', 'mini_text', 'logo')

    def get_address(self, obj):
        return self.get_translated_field(obj, 'address')
    
class BlogSerializer(ModelSerializer,GeneralMixin):
    title = SerializerMethodField()
    description = SerializerMethodField()

    class Meta:
        model = Blog
        fields = ('slug','title','description','image','is_active')

    def get_title(self,obj):
        return self.get_translated_field(obj,'title')
    def get_description(self,obj):
        return self.get_translated_field(obj,'description')
    
class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ('name','phone','active')
    