from typing import List
from django.shortcuts import render
from restaurant.models import Restaurant,MenuItem
from restaurant import serializers
from rest_framework.views import APIView
from restaurant.serializers import Restaurantserializer,MenuItemSerializer,RestaurantListserializer
from rest_framework.views import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from collections import namedtuple
from rest_framework import viewsets

from django.http import JsonResponse
# Create your views here.

# Get Restaurant List
@permission_classes((permissions.IsAuthenticated,))
class RestaurantListView(APIView):
    def get (self,request):
        rest = Restaurant.objects.all()
        
        serializer = RestaurantListserializer(rest,many=True)
        return Response({"Restaurant_List":serializer.data})

# Add  Restaurant List
@permission_classes((permissions.AllowAny,))
class RestaurantView(APIView):
    def get (self,request):
        rest = Restaurant.objects.all()
        
        serializer = Restaurantserializer(rest,many=True)
        return Response({"Restaurant_List":serializer.data})

    def post(self,request):
        serializer = Restaurantserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer._errors,status=status.HTTP_400_BAD_REQUEST)

# Get  MenuItem List
@permission_classes((permissions.AllowAny,))
class MenuItemApiView(APIView):
    def get(self,request,format=None):
        rest = MenuItem.objects.all()
        serializer = MenuItemSerializer(rest,many=True)
        data = serializer.data
        return Response({'statu':data})

    def post(self,request):
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer._errors,status=status.HTTP_400_BAD_REQUEST)


































