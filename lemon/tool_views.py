from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
import method, requests
import json, time, os


def handel_excel(request):
    if request.POST:
        parma = request.POST.get("parma", None)
        file = request.POST.get("file", None)
    swipe = "python E:\\python\\tools\\format\\format_excel.py " + file + " " + parma
    re = os.popen(swipe)
    return HttpResponse(swipe)

def handel_csv(request):
    if request.POST:
        parma = request.POST.get("parma", None)
        file = request.POST.get("file", None)
    swipe = "python E:\\python\\tools\\format\\format_csv.py " + file + " " + parma
    re = os.popen(swipe)
    return HttpResponse(swipe)

def save_case(request):
    if request.POST:
        parma = request.POST.get("parma", None)
        file = request.POST.get("file", None)

    swipe = "python E:\\python\\tools\\lemon\\save_case.py " + file + " " + parma
    re = os.popen(swipe)
    return HttpResponse(swipe)
