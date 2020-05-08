from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Account
from .forms import *
from django.contrib.auth import authenticate, login, logout as dlogout

def ajaxsignup(request):
    ajax = AjaxSignUp(request.POST)
    return JsonResponse(ajax.validate(), safe=False)

def ajaxlogin(request):
    ajax = AjaxLogin(request.POST)
    is_logged, response = ajax.validate()
    if is_logged != False:
        login(request, is_logged)
    return JsonResponse(response, safe=False)

def login(request):
    return render(request,'index.html')

def signup(request):
    return render(request, 'sign-up.html')
