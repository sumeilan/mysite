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
from lemon import views, tool_views
from lemon import views2

urlpatterns = [
    path('index/', views.Page.as_view(page="index.html"), name='index'),
    path('base/', views.Page.as_view(page="base.html"), name='base'),
    path('test/', views.Page.as_view(page="test.html"), name='test'),
    path('slide/', views.Page.as_view(page="slide.html"), name='slide'),
    path('tools/', views.Page.as_view(page="tools.html"), name='tools'),
    path('follow/', views.Page.as_view(page="follow.html"), name='follow'),
    path('excel/', views.Page.as_view(page="excel.html"), name='excel'),
    path('csv/', views.Page.as_view(page="csv.html"), name='csv'),
    path('testcase/', views.Page.as_view(page="testcase.html"), name='testcase'),
    path('api_test/', views.Page.as_view(page="api_test.html"), name='api_test'),
    path('testcase_report/', views.Page.as_view(page="testcase_report.html"), name='testcase_report'),
    path('testp/', views.testp),
    path('connect_adb/', views.connect_adb),
    path('handel_excel/', tool_views.handel_excel),
    path('handel_csv/', tool_views.handel_csv),
    path('save_case/', tool_views.save_case),
    path('report/', tool_views.report),
    path('case_module/',tool_views.case_module),
    path('local_file/', tool_views.local_file),
    path('run_all/', tool_views.run_all),
]
