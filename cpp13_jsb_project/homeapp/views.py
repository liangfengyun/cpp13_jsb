#coding:utf-8
from django.shortcuts import render
# from django.http import HttpResponse
from homeapp.models import TTest

# Create your views here.
def index(request):
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
        }
    }


    return render(request, "homeapp/index.html", obj1)
