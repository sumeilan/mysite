from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
import method, requests
import json, time, os

def handel_excel(request):
    if request.POST:
        parma = request.POST.get("parma", None)
    swipe = "python E:\\test_python\\tools\\format_excel.py " + parma
    re = os.popen(swipe)
    return HttpResponse(swipe)
