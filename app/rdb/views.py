from django.shortcuts import render
from django.http import HttpResponse
from rdb.models import Node, Repeater
from rdb.forms import RepeaterForm

def index(request):
    ctx = {"numrepeaters": Node.objects.count()
            }
    return render(request = request, template_name="home.html", context=ctx )

def repeaters(request):
    ctx = {
            'repeaters':Repeater.objects.all()
            }
    return render(request = request, template_name="repeater/list.html", context=ctx )

def repeater_new(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RepeaterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RepeaterForm()
    ctx = {
            'form':form
            }
    return render(request = request, template_name="repeater/new.html", context=ctx )
