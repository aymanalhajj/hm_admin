from django.urls import path

from django.urls import include
from . import views

urlpatterns = [
    path('register/',views.user_register),
    path('login/',views.user_login),
    path('get_token',views.obtain_token),
]