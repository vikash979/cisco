from django.db import models
from django.conf import settings

from django.contrib.auth import get_user_model



class RouterDetails(models.Model):
    sapid =  models.IntegerField()
    ip = models.GenericIPAddressField(unique=True)
    hostname = models.CharField(max_length=10, blank=True, null=True)
    macaddress = models.CharField(max_length=50, blank=True, null=True)
    


