from django.db import models

# Create your models here.
class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=50)
    city =  models.CharField(max_length=50)
    pincode = models.IntegerField(default=0)
    total_like = models.IntegerField(default=0)
    def __str__(self):
        return self.restaurant_name

class MenuItem(models.Model):
    restaurants = models.ForeignKey(Restaurant, related_name='MenuItem',on_delete=models.CASCADE,default=1)
    dish_name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    total_like = models.IntegerField(default=0)
    total_save = models.IntegerField(default=0)
    def __str__(self):
        return str(self.restaurants)

