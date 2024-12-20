from django.urls import path
from main.views.title import Titles
from main.views.product import ProductView,HeaderView
from main.views.about import AboutView
from main.views.miniview import MiniView,SendMSG
from main.views.video_blog import GetVideo,GetBlog,FooterView


urlpatterns = [
    path('titleview/<str:lang>/', Titles.as_view(), name='title_view'),  # Title view
    path('product/<str:lang>/', ProductView.as_view(), name='product_view'),  # Product view
    path('sliderheader/<str:lang>/', HeaderView.as_view(), name='slider_header_view'),  # Header view for slider
    path('about/<str:lang>/', AboutView.as_view(), name='about_view'),  # About page view
    path('others/<str:lang>/', MiniView.as_view(), name='other_view'),  # Other content view
    path('main_vido_blogs/<str:lang>/', GetVideo.as_view(), name='video_and_blog_view'),  # Video and blog view
    path('get_blog_all_or_get_blog_with_slug/<str:lang>/', GetBlog.as_view(), name='blog_view'),  # Get blog by slug or all blogs
    path('footer/<str:lang>/', FooterView.as_view(), name='footer_view'),  # Footer view
    path('send_message/<str:lang>/<str:name>/<str:phone>/', SendMSG.as_view(), name='footer_view'),
]
