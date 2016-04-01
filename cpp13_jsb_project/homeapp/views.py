#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from homeapp.BLL.ttest_service import ttest_service

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
        allmodels = ttest_service.selectall()
        obj1 = {
            "viewmodel":{
                "name":"zjr",
                "age":28,
                "models":allmodels,
                "pageIndex":pageIndex,
            }
        }

        return render(request, "homeapp/index.html", obj1)
