#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from homeapp.BLL.ttest_service import ttest_service
from django.db import transaction
import uuid
from homeapp.models import TTest
from homeapp.models import TTest2

"""
class article:
    @staticmethod
    haha this is my etst2
    def index(request):
        return HttpResponse("this is article index!")
"""

def update(request):
    if request.method == "POST":

        # update model
        updatingmodel = {
            "guid":request.POST.get("guid"),
            "uname":request.POST.get("uname"),
            "upwd":request.POST.get("upwd"),
        }
        ttest_service.update(updatingmodel)

        # redirect to index
        return HttpResponseRedirect("/homeapp/index")
    else:
        toupdateguid = request.GET.get("guid")
        model = ttest_service.select(toupdateguid)
        print model
        model = {
            "guid":model.guid,
            "uname":model.uname,
            "upwd":model.upwd,
        }

        return render(request, "homeapp/update.html", model)

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
        newTTestguid = str(uuid.uuid1())
        willaddTTest = TTest(guid=newTTestguid
                             , uname=request.POST.get("uname")
                             , upwd = request.POST.get("upwd"))
        willaddTTest2 = TTest2(guid=str(uuid.uuid1())
                               , rname=request.POST.get("rname")
                               , pguid=newTTestguid)
        with transaction.atomic():
            try:
                willaddTTest.save()
                willaddTTest2.save()
            except:
                pass

        return HttpResponse("ca")
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
