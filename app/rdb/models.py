from django.db import models
from django.contrib.auth import get_user_model

#All frequencies in MHz, please

class Node(models.Model):
    callsign = models.CharField(max_length=128)
    owner = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField("Tag")
    add = models.DateTimeField(auto_now_add=True)

    #WGS84 please (if you don't know for sure, you're probably fine)
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
        return "%s (%f-%f)"%(self.name, self.frequency_lo, self.frequency_hi)

class LicenseType(Tag):
    pass
    
    
