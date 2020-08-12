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
