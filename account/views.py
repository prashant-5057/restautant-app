import json
from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from account.serializers import User, UserRegstrationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken
from restaurant.models import MenuItem, Restaurant
# Create your views here.

@permission_classes((permissions.AllowAny,))
class RegiterApiView(APIView):
    serializer_class = UserRegstrationSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user= serializer.save()
            resfresh = RefreshToken.for_user(user)
            response_data = {'refresh':str(resfresh),'access':str(resfresh.access_token)}
            # serializer_data = serializer.data
            return Response(response_data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@permission_classes((permissions.AllowAny,))
class UserRestaurantView(APIView):
    def post(self,request):
        is_like = request.query_params.get('is_like')
        restautant_obj = Restaurant.objects.filter(id=request.data['restaurant_id']).first()
        user = request.user
        if restautant_obj:
            print(restautant_obj)
            user.like.add(restautant_obj.id) if is_like == 'True' else user.like.remove(restautant_obj.id)
        return Response({"Status":True})
@permission_classes((permissions.AllowAny,))
class UserRestaurantSaveView(APIView):
    def post(self,request):
        is_save = request.query_params.get('is_save')
        restautant_obj = Restaurant.objects.filter(id=request.data['restaurant_id']).first()
        user = request.user
        if restautant_obj:
            # print(restautant_obj)
            user.save_post.add(restautant_obj.id) if is_save == 'True' else user.save_post.remove(restautant_obj.id)
            # print('****',user)
        return Response({"status":True})

@permission_classes((permissions.AllowAny,))
class UsermenulikeView(APIView):
    def post(self,request):
        is_like = request.query_params.get('is_like')
        restautant_obj = MenuItem.objects.filter(id=request.data['menuitem_id']).first()
        user = request.user
        if restautant_obj:
            print(restautant_obj)
            user.like_menu.add(restautant_obj.id) if is_like == 'True' else user.like_menu.remove(restautant_obj.id)
        return Response({"Status":True})

@permission_classes((permissions.AllowAny,))
class UsermenuSaveView(APIView):
    def post(self,request):
        is_save = request.query_params.get('is_save')
        restautant_obj = MenuItem.objects.filter(id=request.data['menuitem_id']).first()
        user = request.user
        if restautant_obj:
            # print(restautant_obj)
            user.save_menu.add(restautant_obj.id) if is_save == 'True' else user.save_menu.remove(restautant_obj.id)
            # print('****',user)
        return Response({"status":True})

@permission_classes((permissions.AllowAny,))
class UserDetail(APIView):
    def get(self,request):
        user = request.user

        restautant_obj = user.like.all()
        
        # obj = user.like(restautant_obj)
        # id=request.data
        user_obj = User.like.get['user_id']
        # print(restautant_obj)
        return Response({"status":True,"user_like":user_obj})

    # def get(self,request):
    #     user_id = User.objects.get('like')
    #     likes = User.like.filter(USer_id=user_id)
        # queryset = User.objects.all()
        # user_obj = request.user
        # pbj = user_obj.id
        # print('*****',likes)
        # restautant_obj=user_obj.like.filter('user_id')
        # restautant_obj = id=request.data('user_id')
        # print(restautant_obj,'*************')
        # print("******qwer*****",qwer)
        # for likes in queryset:  
        #     obj = likes.like.all()
        #     print(obj)
        # return Response({"status":True})
    # def get_queryset(self):
    #     user = self.request.user
    #     adaccount_list = User.objects.filter(user=user)\
    #                      .values_list('like', flat=True)
    #     return MenuItem.objects.filter(adaccount__in=adaccount_list)
    # def get(request,id):
 
 
    #     user_id = User.objects.all()
    #     for i in user_id:
    #         print(i)

        # likes= User.like.filter(user_id=id)
        # print(user_id)
        # users_participe=[]
        # for i in likes:
        #     b=i.users_id
        #     print(b)
            # c=(b.id,b.menuitem_id)
            # users_participe.append(c)
        # return Response({'users_participe':True})