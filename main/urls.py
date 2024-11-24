from django.urls import path
from main.views.about import CandidateView,CandidateUpdate,LoginView,LogoutView,SearchView

urlpatterns = [
    path('candidateview/', CandidateView.as_view(), name='candidateview'),
    path('candidateview/<int:id>/', CandidateUpdate.as_view(), name='candidateview'),
    path('login/',LoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(), name='login'),
    path('search/',SearchView.as_view(), name='login'),



]
