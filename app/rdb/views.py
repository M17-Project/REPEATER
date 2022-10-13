from django.shortcuts import render
from django.http import HttpResponse
from rdb.models import Node

def index(request):
    ctx = {"numrepeaters": Node.objects.count()
            }
    return render(request = request, template_name="home.html", context=ctx )

