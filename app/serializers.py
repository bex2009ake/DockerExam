from rest_framework.serializers import ModelSerializer
from app.models import *
from django.contrib.auth.models import User



class UserApi(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ContactApi(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class AboutApi(ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'