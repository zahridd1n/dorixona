from django.urls import path
from main.views.about import Titles
from main.views.product import ProductView


urlpatterns = [
    path('candidateview/<str:lang>/', Titles.as_view(), name='candidateview'),
    path('product/<str:lang>/', ProductView.as_view(), name='candidateview'),

    # path('candidateview/<int:id>/', CandidateUpdate.as_view(), name='candidateview'),
    # path('login/',LoginView.as_view(), name='login'),
    # path('logout/',LogoutView.as_view(), name='login'),
    # path('search/',SearchView.as_view(), name='login'),



]
