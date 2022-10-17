"""repeater URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings 
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('rdb/', include('rdb.urls')),
    path('', include('rdb.urls')),
    path('api', include('rest.urls')),
    path('api/', include('rest.urls')),

    re_path(r"^" +settings.STATIC_URL.strip('/')  + r"/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}), 
    #fly static files can take a long time to
    # settle on a deploy, and meanwhile django will 404 otherwise. So
    # we don't expect to serve static files all the time in production
    # with this rule, but it is necessary at least some times because of
    # fly.io idiosyncrasy.
]
urlpatterns += staticfiles_urlpatterns()
