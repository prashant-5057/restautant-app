from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from account import views
urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/',views.RegiterApiView.as_view()),
    path('like/',views.UserRestaurantView.as_view()),
    path('save_post/', views.UserRestaurantSaveView.as_view()),
    path('menulike/',views.UsermenulikeView.as_view()),
    path('menusave/',views.UsermenuSaveView.as_view()),
    path('detail/',views.UserDetail.as_view())

]