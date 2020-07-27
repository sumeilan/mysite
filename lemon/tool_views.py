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
    file = 'E:\\python\\testcase\\report'
    data = '{"code":0,"msg":"","count":10,"data":[{"id":10,"file":"2020-07-27.html","option":"查看"},{"id":10,"file":"2020-07-27.html","option":"查看"}]}'
    swipe = "python E:\\python\\tools\\lemon\\get_file.py " + file
    re = os.popen(swipe)
    return HttpResponse(re)

def local_file(request):
    fil = request.POST.get("file", None)
    file = "E:\\python\\testcase\\report\\" + fil
    swipe = "python E:\\python\\tools\\local_file.py " + file
    re = os.popen(swipe)
    return HttpResponse(swipe)