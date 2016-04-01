#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from homeapp.models import TTest

# Create your views here.
def index(request):

    if request.method == "POST":

        obj1 = {
            "viewmodel":{
                "uname":request.POST.get("uname"),
                "upwd":request.POST.get("upwd"),
            }
        }

        return HttpResponse(obj1["viewmodel"]["uname"] + obj1["viewmodel"]["upwd"])
    else:

        pageIndex = request.GET.get("pageIndex");

        # return HttpResponse("hello, jsb")
        obj1 = {
             "viewmodel":{
                "name":"zjr",
                "age":28
             }
        }

        # 从这里开始，是查询数据库的测试语句
        # testmodel = TTest.objects.all()[0]
        allmodels = TTest.objects.all()
        obj1 = {
            "viewmodel":{
                "name":"zjr",
                "age":28,
                "models":allmodels,
                "pageIndex":pageIndex,
            }
        }

        return render(request, "homeapp/index.html", obj1)
