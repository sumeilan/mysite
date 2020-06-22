"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # path('index/',views.index, name='index'),
    path('index/', views.Page.as_view(page="index.html"), name='index'),
    path('test/', views.Page.as_view(page="test1.html"), name='test'),
    path('lemon/', views.Page.as_view(page="lemon.html"), name='lemon'),
    path('testcase/', views.Page.as_view(page="testcase.html"), name='testcase'),
    url('add/', views.post),
    path('testp/', views.testp),
    path('testapi/', views.testapi),
    path('connect_adb/', views.connect_adb),
]
