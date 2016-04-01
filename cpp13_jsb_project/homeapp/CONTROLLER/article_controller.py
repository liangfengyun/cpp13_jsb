#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from homeapp.BLL.ttest_service import ttest_service

class article:

    @staticmethod
    def index(request):
        return HttpResponse("this is article index!")

