from django.db import models

# Create your models here.
class TTest(models.Model):

    guid=models.CharField(max_length=36, primary_key=True)
    uname=models.CharField(max_length=50, null=True)
    upwd=models.CharField(max_length=50, null=True)

    def __unicode__(self):
        return self.guid
