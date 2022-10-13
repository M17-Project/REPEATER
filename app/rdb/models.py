from django.db import models
from django.contrib.auth import get_user_model
import math
#All frequencies in MHz, 
#distances and altitudes in m
#lat,lon in wgs84

def get_band(freq):
    if freq > 400 and freq < 470:
        return "70cm"
    if freq > 140 and freq < 148:
        return "2m"

def get_std_offset(band):
    if band == "2m":
        return 0.6
    if band == "70cm":
        return 5

class DuplexFrequencyPair(models.Model):
    tags = models.ManyToManyField("Tag")
    in_freq = models.FloatField()
    out_freq = models.FloatField()
    def __str__(self):
        offset = self.in_freq-self.out_freq
        b1,b2 = get_band(self.in_freq),get_band(self.out_freq)
        sign = ""
        if offset >= 0:
            sign = "+"
        print(b1,b2,offset)
        if b1==b2 and math.isclose(get_std_offset(b1), abs(offset)):
            if offset < 0:
                sign = "-"
            return "%g%s"%(self.out_freq, sign)
        return "%g%s%g"%(self.out_freq, sign, offset)


class Node(models.Model):
    callsign = models.CharField(max_length=128)
    owner = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField("Tag")
    add = models.DateTimeField(auto_now_add=True)

    lat = models.FloatField()
    lon = models.FloatField()
    alt = models.FloatField()

    @property
    def location(self):
        return [self.lat, self.lon]
    def __str__(self):
        try: 
            owner=self.owner.username
        except:
            owner = "<no owner>"
        return "[%s] %s %s"%(owner, self.callsign, str(self.location))

class Repeater(Node):
    freq = models.ManyToManyField("DuplexFrequencyPair")
    access_information = models.TextField() #temp

class Tag(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True)
    def __str__(self):
        return "%s"%(self.name)

class Band(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True)
    licensetype = models.ManyToManyField("LicenseType")
    frequency_lo = models.FloatField()
    frequency_hi = models.FloatField()

    @property
    def bw(self):
        return self.frequency_hi - self.frequency_low
    def __str__(self):
        return "%s (%g-%g)"%(self.name, self.frequency_lo, self.frequency_hi)

class LicenseType(Tag):
    pass
    
    
