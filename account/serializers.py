from dataclasses import field, fields
from pyexpat import model
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
# from account.models import Res
User = get_user_model()

class UserRegstrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True)
    password2= serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['email','password','password2']
        # extra_kwargs =  {}

    def create(self, validated_data):
       
        email = validated_data.get('email')
        password = validated_data.get('password')
        password2 = validated_data.get('password2')

        if password==password2:
            user = User(email=email)
            user.set_password(password)
            user.save()
            return user
        else:
            raise serializers.ValidationError({'error':'password invald'})

