from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from app.models import *
from app.serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
# Create your views here.



class Register(APIView):
    def get(self, req:Request):
        return Response({'msg': 'register'})
    
    def post(self, req:Request):
        username = req.data.get('username')
        password = req.data.get('password')

        if bool(username) == False:
            return Response({'msg':'Something wrong in username'})
        
        if bool(password) == False:
            return Response({'msg':'Something wrong in password'})
        
        user = User.objects.create_user(username=username, password=password)

        token = RefreshToken.for_user(user=user)

        print({
            'access_token': str(token.access_token),
            'refresh_token': str(token)
        })

        return Response({
            'access_token': str(token.access_token),
            'refresh_token': str(token)
        })
        

class Login(APIView):
    def get(self, req:Request):
        return Response({'msg': 'Login'})
    
    def post(self, req:Request):
        username = req.data.get('username')
        password = req.data.get('password')

        if bool(username) == False:
            return Response({'msg':'Something wrong in username'})
        
        if bool(password) == False:
            return Response({'msg':'Something wrong in password'})
        
        user = User.objects.all().filter(username=username).first()
        if bool(user) == False:
            return Response({'msg': 'This user doesn`t exist'})
    
        token = RefreshToken.for_user(user=user)
            
        return Response({
            'access_token': str(token.access_token),
            'refresh_token': str(token)
        })
        

class ReadContact(ListAPIView):
    serializer_class = ContactApi
    queryset = Contact.objects.all()


class CreateContact(CreateAPIView):
    serializer_class = ContactApi
    queryset = Contact.objects.all()


class ReadAbout(ListAPIView):
    serializer_class = AboutApi
    queryset = About.objects.all()


class CreateAbout(CreateAPIView):
    serializer_class = AboutApi
    queryset = About.objects.all()

@api_view(http_method_names=['get'])
def searchAbout(req:Request, title):
    db = About.objects.all().filter(title=title).first()


    if bool(db) == False:
        return Response({'msg':'No'})

    return Response({'about': db.title})

# {
#   "username": "Behruz",
#   "password": "Password123$$"
# }