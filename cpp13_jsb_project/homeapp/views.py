from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("hello, jsb")
    obj1 = {
        "viewmodel":{
            "name":"zjr",
            "age":28
        }
    }
    return render(request, "homeapp/index.html", obj1)
