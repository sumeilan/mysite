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
from lemon import views,tool_views
from lemon import views2

urlpatterns = [
    # path('index/',views.index, name='index'),
    path('index/', views.Page.as_view(page="index.html"), name='index'),
    path('test/', views.Page.as_view(page="test1.html"), name='test'),
    path('lemon/', views.Page.as_view(page="lemon.html"), name='lemon'),
    path('excel/', views.Page.as_view(page="excel.html"), name='excel'),
    path('csv/', views.Page.as_view(page="csv.html"), name='csv'),
    path('testcase/', views.Page.as_view(page="testcase.html"), name='testcase'),
    path('api_test/', views.Page.as_view(page="api_test.html"), name='api_test'),
    url('add/', views2.post),
    path('testp/', views.testp),
    path('testapi/', views2.testapi),
    path('connect_adb/', views.connect_adb),
    path('handel_excel/', tool_views.handel_excel),
    path('handel_csv/', tool_views.handel_csv),
    path('save_case/', tool_views.save_case),
    path('report/',tool_views.report),
]
