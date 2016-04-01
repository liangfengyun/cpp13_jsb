#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from homeapp.BLL.ttest_service import ttest_service

def delete(request):
    todelguid = request.GET.get("guid")
    ttest_service.delete(todelguid)

    # 显示index页面
    return HttpResponseRedirect("/homeapp/index")

def add(request):
    if request.method == "POST":
        print "this is post query"
        # 添加到数据库
        addingmodel = {
            "uname":request.POST.get("uname"),
            "upwd":request.POST.get("upwd"),
        }

        ttest_service.add(addingmodel)

        # 显示index页面
        return HttpResponseRedirect("/homeapp/index")
    else:
        print "this is get query"
        return render(request, "homeapp/add.html", {})

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
