from dataclasses import fields
from rest_framework  import serializers
from restaurant.models import Restaurant,MenuItem
from restaurant.models import Restaurant,MenuItem
from rest_framework.views import Response

# create the serializers Classess

# Get the Restaurant List serializers
class  RestaurantListserializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id','restaurant_name','city','pincode','total_like']

# Get the Restaurant List serializers
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['restaurants','dish_name','price','total_like','total_save']
            

# Get the Restaurant_MenuItem List serializers
class  Restaurantserializer(serializers.ModelSerializer):
    MenuItem = MenuItemSerializer(many=True,read_only=True)
    class Meta:
        model = Restaurant
        fields = ['id','restaurant_name','city','pincode','total_like','MenuItem']
            
        



        




