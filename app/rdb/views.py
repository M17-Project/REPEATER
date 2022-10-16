from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from rdb.models import Node, Repeater
from rdb.forms import RepeaterForm

import csv
import datetime

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

def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename=RepeaterData'+str(datetime.datetime.now())+'.csv'

    writer = csv.writer(response)
    writer.writerow(['Index', 'Repeater','Owner', 'Callsign', 'Frequency', 'Location','AccessInformation', 'Added', 'Tags' ])

    repeater_list = Repeater.objects.all()
    s_no = 1

    for rep in repeater_list:
        writer.writerow([s_no,
            rep,
            rep.owner,
            rep.callsign,
            rep.freq,
            str(rep.location),
            rep.access_information,
            rep.added,
            rep.tags,])
        s_no+=1
    # Reset S.no in case exported multiple times
    s_no=1

    return response