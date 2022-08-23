from django import views
from django.contrib import admin
from django.urls import path
from restaurant import views
urlpatterns = [
    path('',views.RestaurantView.as_view()),
    path("reslist/",views.RestaurantListView.as_view()),
    path('menu/',views.MenuItemApiView.as_view()),

]
