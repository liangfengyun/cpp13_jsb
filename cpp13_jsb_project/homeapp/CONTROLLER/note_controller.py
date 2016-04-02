#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from homeapp.BLL.ttest_service import ttest_service

class note:

    @staticmethod
    def index(request):

    	pageModel = {
    		"items":[
    			{"guid":"1"},
    			{"guid":"2"},
    			{"guid":"3"},
    			{"guid":"11"},
    			{"guid":"12"},
    			{"guid":"13"},
    			{"guid":"111"},
    			{"guid":"112"},
    			{"guid":"113"},
    		]
    	}








 	return render(request, "homeapp/note_index.html", pageModel)

