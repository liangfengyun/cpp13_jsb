from django.contrib import admin
from homeapp.models import TTest
from homeapp.models import TTest2
from homeapp.models import TAccount
from homeapp.models import TNote
from homeapp.models import TNoteType
from homeapp.models import TLog
from homeapp.models import RTLog_TNote



# Register your models here.
admin.site.register(TTest)
admin.site.register(TTest2)
admin.site.register(TAccount)
admin.site.register(TNote)
admin.site.register(TNoteType)
admin.site.register(TLog)
admin.site.register(RTLog_TNote)

