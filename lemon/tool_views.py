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

    swipe = "python E:\\test_python\\tools\\lemon\\save_case.py " + file + " " + parma
    re = os.popen(swipe)
    return HttpResponse(swipe)

def report(request):
    data = '{"code":0,"msg":"","count":10,"data":[{"id":10,"time":"2020/07/26 16:20","option":"查看"}]}'
    return HttpResponse(data)
