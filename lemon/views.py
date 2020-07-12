from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
import method, requests
import json, time, os


class Page(View):
    page = "index.html"
    def get(self,request):
        return render(request, self.page)

def send_url(env, path, header, body):
    # url = 'http://lemondream.chumanapp.com/api/banner/get_banner_list'
    if env == 'demo':
        url = 'http://lemondream.chumanapp.com' + path
    elif env == 'api2':
        url = 'http://api-api2.lemondream.cn' + path
    else:
        url = 'http://api.lemondream.cn' + path

    body = body
    headers = eval(header)
    response = requests.post(url, body, headers=headers, verify=False)
    return HttpResponse(response, content_type="application/json")


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

        return HttpResponse(u'方法不对')


def connect_adb(request):
    #swipe = "adb shell input swipe 500 1000 500 10"
    swipe = "adb devices"
    re = os.popen(swipe)
    return HttpResponse(re)

def save_case(request):
    return HttpResponse('done')