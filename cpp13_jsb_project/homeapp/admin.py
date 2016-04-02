from django.contrib import admin
from homeapp.models import TTest
from homeapp.models import TTest2
from homeapp.models import TAccount
from homeapp.models import TNote
from homeapp.models import TNoteType
from homeapp.models import TLog



# Register your models here.
admin.site.register(TTest)
admin.site.register(TTest2)
admin.stte.register(TAccount)
admin.stte.register(TNote)
admin.stte.register(TNoteType)
admin.stte.register(TLog)

