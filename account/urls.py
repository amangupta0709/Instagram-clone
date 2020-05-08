from django.urls import path
from account import views

urlpatterns = [
    path('', views.login, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('ajaxsignup', views.ajaxsignup, name='ajaxsignup'),
    path('ajaxlogin', views.ajaxlogin, name='ajaxlogin')
]