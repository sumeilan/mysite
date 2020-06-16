from django.http import HttpResponse
from django.shortcuts import render
import method,requests
import json


def index(request):
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
    return render(request, "index.html", {"data": data, "data1": data1, "title": title})


def add_args(a, b):
    x = int(a)
    y = int(b)
    return x + y

def send_url(url):
    url = 'http://lemondream.chumanapp.com/api/sample/test_sendcode?mobile=88850769071'
    params = {'a': 'a', 'b': 'b'}
    headers ={'versionCode': 'android_1.9.3', 'Content-Type': 'application/json', 'X-Token': '4b5d4b5e0044'}
    response = requests.post(url,  headers=headers, verify=False)
    return HttpResponse(response.text)


def testp(request):
    if request.method == 'POST':
        if request.POST:
            body = request.POST.get('body', None)
            url = request.POST.get('url', None)
            res = send_url(url)
            return HttpResponse(res)
        else:
            return HttpResponse(u'输入为空')
    else:
        a = request.GET['a']
        res = send_url(a)
        return HttpResponse(res)


def test(request):
    return render(request, 'test1.html')

def testcase(request):
    return render(request, 'testcase.html')

def post(request):
    if request.method=='POST':
        d={}
        if request.POST:
            a=request.POST.get('a',None)
            b=request.POST.get('b',None)
            if a and b:
                res=add_args(a, b)
                d['message1']=res
                d=json.dumps(d)
                return HttpResponse(d)
            else:
                return HttpResponse(u'输入错误')
        else:
            return HttpResponse(u'输入为空')
    else:
        return HttpResponse(u'方法错误')


def testcasepP(request):
    pt = method.cls_api()
    expect_reusult = request.POST.get('expect_reusult', None)
    data = ""
    data1 = ""
    if request.method == 'POST':
        data = pt.post(request.POST.get('url', None), json.loads(request.POST.get('testdate', None)))
        result = data.json()
        data1 = result['message']
        if int(result['message'] == int(expect_reusult)):
            data = 'pass'
        else:
            data = 'fail'
    return HttpResponse(data)

