from django.urls import path
from main.views.title import Titles
from main.views.product import ProductView,HeaderView
from main.views.about import AboutView
from main.views.miniview import MiniView



urlpatterns = [
    path('titleview/<str:lang>/', Titles.as_view(), name='candidateview'),
    path('product/<str:lang>/', ProductView.as_view(), name='candidateview'),
    path('sliderheader/<str:lang>/', HeaderView.as_view(), name='candidateview'),
    path('about/<str:lang>/', AboutView.as_view(), name='candidateview'),
    path('others/<str:lang>/', MiniView.as_view(), name='candidateview'),


    # path('candidateview/<int:id>/', CandidateUpdate.as_view(), name='candidateview'),
    # path('login/',LoginView.as_view(), name='login'),
    # path('logout/',LogoutView.as_view(), name='login'),
    # path('search/',SearchView.as_view(), name='login'),



]
