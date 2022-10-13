from django.forms import ModelForm
from rdb.models import *

class RepeaterForm(ModelForm):
    class Meta:
        model = Repeater
        fields = ['callsign','tags', 'lat','lon','alt', 'freq','access_information']
