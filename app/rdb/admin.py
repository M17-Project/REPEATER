from django.contrib import admin

from rdb.models import *
for each in [Node,Tag,Band,LicenseType]:
    admin.site.register(each)
