#coding:utf-8
from django.db import models

# Create your models here.

# 用户的记述宝帐号表 ####################################
class TAccount(models.Model):

    guid=models.CharField(max_length=36, primary_key=True)
    openid=models.CharField(max_length=100, null=True)
    nickname=models.CharField(max_length=50, null=True)
    sex=models.NullBooleanField(null=True)
    language=models.CharField(max_length=50, null=True)
    city=models.CharField(max_length=50, null=True)
    province=models.CharField(max_length=50, null=True)
    country=models.CharField(max_length=50, null=True)
    headimgurl=models.CharField(max_length=100, null=True)
    subscribe_time=models.DateTimeField(null=True)
    unionid=models.CharField(max_length=100, null=True)
    remark=models.NullBooleanField(null=True)
    groupid=models.CharField(max_length=50, null=True)

    def __unicode__(self):
        return self.guid

# #######################################################

# 用户的记述表 ##########################################
class TNote(models.Model):

    guid=models.CharField(max_length=36, primary_key=True)
    Account_Guid=models.CharField(max_length=36)
    NoteDateTime=models.DateTimeField(null=True)
    Path=models.CharField(max_length=100, null=True)
    Text=models.CharField(max_length=50, null=True)
    NoteType_Guid=models.CharField(max_length=36, null=True)

    def __unicode__(self):
        return self.guid

# #######################################################

# 记述类型表 ############################################
class TNoteType(models.Model):

    guid=models.CharField(max_length=36, primary_key=True)
    TypeName=models.CharField(max_length=50, null=True)

    def __unicode__(self):
        return self.guid

# #######################################################

# 日志表 ################################################
class TLog(models.Model):

    guid=models.CharField(max_length=36, primary_key=True)
    Title=models.CharField(max_length=50, null=True)
    LogDateTime=models.DateTimeField(null=True)

    def __unicode__(self):
        return self.guid

# #######################################################

# 外键表 日志_记述表 ####################################
class RTLog_TNote(models.Model):

    guid=models.CharField(max_length=36, primary_key=True)
    Log_Guid=models.CharField(max_length=36, null=True)
    Note_Guid=models.CharField(max_length=36, null=True)
    order=models.IntegerField(null=True)

    def __unicode__(self):
        return self.guid

# #######################################################




# 测试表 TTest
class TTest(models.Model):

    guid=models.CharField(max_length=36, primary_key=True)
    uname=models.CharField(max_length=50, null=True)
    upwd=models.CharField(max_length=50, null=True)

    def __unicode__(self):
        return self.guid

# 测试表 TTest2
class TTest2(models.Model):

    guid=models.CharField(max_length=36, primary_key=True)
    rname=models.CharField(max_length=50, null=True)
    pguid=models.CharField(max_length=50)

    def __unicode__(self):
        return self.guid
