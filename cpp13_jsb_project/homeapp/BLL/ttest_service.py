#coding:utf-8
# from homeapp.models import TTest
from homeapp.DAL.ttest_dal import ttest_dal

class ttest_service():

    @staticmethod
    def selectall():
        objs = ttest_dal.selectall()
        return objs

    @staticmethod
    def add(addingmodel):
        ret = ttest_dal.add(addingmodel)
        return ret

    @staticmethod
    def delete(todelguid):
        ret = ttest_dal.delete(todelguid)
        return ret
