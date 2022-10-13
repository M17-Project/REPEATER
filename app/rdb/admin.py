from django.contrib import admin

from rdb.models import *
for each in [Node,Repeater,DuplexFrequencyPair,Tag,Band,LicenseType]:
    admin.site.register(each)
