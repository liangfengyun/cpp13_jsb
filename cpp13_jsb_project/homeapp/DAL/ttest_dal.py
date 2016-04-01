#coding:utf-8
from homeapp.models import TTest
import uuid

# import connection
# from django.db import connection

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
        """
        objs = TTest.objects.all()
        return objs
        """
        # paraint1 = "11 or 1 = 1"
        paraint1 = str(1)

        raw_sql = "select guid, uname, upwd, 'a' as haha from homeapp_ttest where 1 = %s"
        raw_querySet = TTest.objects.raw(raw_sql, [ paraint1 ])
        return raw_querySet

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
