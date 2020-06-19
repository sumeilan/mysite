from django.http import HttpResponse
from django.shortcuts import render
import method, requests
import json


def testapi(request):
    pt = method.cls_api()
    exr = request.POST.get('exr', None)
    title = "这么久没见2"
    data = ""
    data1 = ""
    if request.method == 'POST':
        data = pt.post(request.POST.get('url', None), json.loads(request.POST.get('testdate', None)))
        result = data.json()
        data1 = result['message']
        if int(result['message'] == int(exr)):
            data = 'pass'
        else:
            data = 'fail'
    return render(request, "testapi.html", {"data": data, "data1": data1, "title": title})


def add_args(a, b):
    x = int(a)
    y = int(b)
    return x + y


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
            return HttpResponse(u'输入为空')
    else:
        a = request.GET['a']
        res = send_url(a)
        return HttpResponse(res)


def post(request):
    if request.method == 'POST':
        d = {}
        if request.POST:
            a = request.POST.get('a', None)
            b = request.POST.get('b', None)
            if a and b:
                res = add_args(a, b)
                d['message1'] = res
                d = json.dumps(d)
                return HttpResponse(d)
            else:
                return HttpResponse(u'输入错误')
        else:
            return HttpResponse(u'输入为空')
    else:
        return HttpResponse(u'方法错误')


def test(request):
    return render(request, 'test1.html')


def index(request):
    return render(request, 'index.html')
