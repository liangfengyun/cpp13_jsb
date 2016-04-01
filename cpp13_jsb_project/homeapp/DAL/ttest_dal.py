#coding:utf-8
from homeapp.models import TTest
import uuid

class ttest_dal():

    @staticmethod
    def select(strguid):
        ret = TTest.objects.get(guid=strguid)
        return ret

    @staticmethod
    def update(updatingmodel):

        toupdatemodel = TTest.objects.get(guid=updatingmodel["guid"])
        toupdatemodel.uname = updatingmodel["uname"]
        toupdatemodel.upwd = updatingmodel["upwd"]
        toupdatemodel.save()

        return 1

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
