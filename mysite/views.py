from django.http import HttpResponse
from django.shortcuts import render
import method
import json


def runoob(request):
    context = {}
    context['hello'] = 'Hello!'
    return render(request, 'runoob.html', context)


def index(request):
    pt = method.cls_api()
    exr = request.POST.get('exr', None)
    title = "这么久没见"
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
    return render(request, "index.html", {"data": data, "data1": data1, "title": title})


def add_args(a, b):
    x = int(a)
    y = int(b)
    return x + y


def post(request):
    if request.method == 'POST':
        d = {}
        if request.POST:
            a = request.POST.get('a', None)
            b = request.POST.get('b', None)
            if a and b:
                res = add_args(a, b)
                d['message'] = res
                d = json.dumps(d)
            else:
                return HttpResponse(u'输入错误')
        else:
            return HttpResponse(u'输入为空')
    else:
        a = request.GET['a']
        b = request.GET['b']
        res = add_args(a, b)

    return HttpResponse(res)


def test(request):
    return render(request, 'test.html')

def add(request):
    a = request.GET['a']
    a1= request.POST.get('a', None)
    b = request.GET['b']
    b1 = request.POST.get('b', None)
    c = int(a) + int(b)
    c1 = int(a1) + int(b1)
    return HttpResponse(str(c1))
