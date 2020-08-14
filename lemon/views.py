from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
import requests
import json, time, os


class Page(View):
    page = "index.html"

    def get(self, request):
        return render(request, self.page)



def send_url(env, path, header, body):
    if env == 'demo':
        url = 'http://api-demo.lemondream.cn' + path
    elif env == 'api2':
        url = 'http://api-api2.lemondream.cn' + path
    else:
        url = 'http://api.lemondream.cn' + path

    body = body
    headers = eval(header)
    response = requests.post(url, body, headers=headers, verify=False)
    print(url)
    return HttpResponse(response)


def testp(request):
    if request.method == 'POST':
        if request.POST:
            env = request.POST.get('env', None)
            path = request.POST.get('path', None)
            header = request.POST.get('header', None)
            body = request.POST.get('body', None)
            res = send_url(env, path, header, body)
            return HttpResponse(res)
        else:
            return HttpResponse(u'输入为空 ')
    else:
        env = request.GET.get('env', None)
        path = request.GET.get('path', None)
        print(env)
        return HttpResponse(env)
