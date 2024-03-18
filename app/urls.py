from django.urls import path
from app.views import *


urlpatterns = [
   path('login/', Login.as_view(), name='login'),
   path('singup/', Register.as_view(), name='register'),
   path('craete-about/', CreateAbout.as_view(), name='create-about'),
   path('craete-contact/', CreateContact.as_view(), name='create-contact'),
   path('read-about/', ReadAbout.as_view(), name='read-about'),
   path('read-contact/', ReadContact.as_view(), name='read-contact'),
   path('about/<str:title>/', searchAbout, name='search'),
]