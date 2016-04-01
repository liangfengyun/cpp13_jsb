#coding:utf-8
from homeapp.models import TTest

class ttest_dal():

    @staticmethod
    def selectall():
        objs = TTest.objects.all()
        return objs
