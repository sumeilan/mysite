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
        file = request.POST.get("case_file", None)
        module = request.POST.get("module", None)
        case_name = request.POST.get("case_name", None)
        url = request.POST.get("c_path", None)
        request_headers = request.POST.get("c_header", None)
        request_parameter = request.POST.get("c_body", None)
        expect_result = request.POST.get("e_result", None)
        request_method = request.POST.get("method", None)


    sheet_id = module
    # case = ["case_name", "module", "url", "request_method", "request_headers", "request_parameter", "expect_result"]
    case = [case_name,module,url,request_method,request_headers,request_parameter,expect_result]
    case = "@".join(case)
    print("case",case)

    swipe = "python E:\\python\\tools\\lemon\\save_case.py " + file + " " + sheet_id + " " + case
    print(swipe)
    re = os.popen(swipe)
    return HttpResponse(swipe)


def report(request):
    file = "E:\\python\\testcase\\report"
    swipe = "python E:\\python\\tools\\lemon\\get_file.py " + file
    re = os.popen(swipe)
    return HttpResponse(re)


def case_module(request):
    file = "E:\\python\\testcase\\data\\case1.xlsx"
    swipe = "python E:\\python\\tools\\lemon\\response_data.py " + file
    re = os.popen(swipe)
    data = '{"code": "0", "msg": "\u64cd\u4f5c\u6210\u529f", "count": 10, "data": [{"id": 1, "name": "Sheet1", "right": "\u6267\u884c"}, {"id": 2,"name": "Sheet2", "right": "\u6267\u884c"}, {"id": 3, "name": "Sheet3", "right": "\u6267\u884c"}]}'
    return HttpResponse(re)

def run_all(request):
    swipe = "python E:\\python\\testcase\\brun.py"
    re = os.popen(swipe)
    return HttpResponse(re)


def local_file(request):
    fil = request.POST.get("file", None)
    param = request.POST.get("param", None)
    file = "E:\\python\\testcase\\report\\" + fil
    swipe = "python E:\\python\\tools\\local_file.py " + file + " " + param
    re1 = os.popen(swipe)
    return HttpResponse(re1)
