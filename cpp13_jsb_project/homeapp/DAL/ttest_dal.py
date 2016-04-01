#coding:utf-8
from homeapp.models import TTest
import uuid

class ttest_dal():

    @staticmethod
    def selectall():
        objs = TTest.objects.all()
        return objs

    @staticmethod
    def add(addingmodel):
        willadd = TTest(guid=str(uuid.uuid1())
                        , uname=addingmodel["uname"]
                        , upwd=addingmodel["upwd"])
        willadd.save()

        return 1

    @staticmethod
    def delete(todelguid):
        arr = TTest.objects.filter(guid=todelguid)
        arr.delete()

        return 1
