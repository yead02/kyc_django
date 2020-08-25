from django.db import models

# Create your models here.
from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.urls import reverse
import uuid


class fxd(models.Model):

    branch = models.CharField(max_length=30,default='Null', blank=True)
    date = models.DateField(blank=True)
    acc_title = models.CharField(max_length=30,default='Null', blank=True)
    toa = models.CharField(max_length=30,default='Null', blank=True)
    cusocc = models.CharField(max_length=30,default='Null', blank=True)
    cuspro = models.CharField(max_length=30,default='Null', blank=True)
    sof = models.CharField(max_length=30,default='Null', blank=True)
    doccol1 = models.CharField(max_length=30,default='Null', blank=True)
    doccol2 = models.CharField(max_length=30,default='Null', blank=True)
    doccol3 = models.CharField(max_length=30,default='Null', blank=True)
    coldocver = models.CharField(max_length=30,default='Null', blank=True)
    addaccver = models.CharField(max_length=30,default='Null', blank=True)
    benownacc = models.CharField(max_length=30,default='Null', blank=True)
    passno = models.CharField(max_length=30,default='Null', blank=True)
    passnorc = models.CharField(max_length=30,default='Null', blank=True)
    passnover = models.CharField(max_length=30,default='Null', blank=True)
    nid = models.CharField(max_length=30,default='Null', blank=True)
    nidrc = models.CharField(max_length=30,default='Null', blank=True)
    nidver = models.CharField(max_length=30,default='Null', blank=True)
    etin = models.CharField(max_length=30,default='Null', blank=True)
    etinrc = models.CharField(max_length=30,default='Null', blank=True)
    etinver = models.CharField(max_length=30,default='Null', blank=True)
    bcer = models.CharField(max_length=30,default='Null', blank=True)
    bcerrc = models.CharField(max_length=30,default='Null', blank=True)
    bcerver = models.CharField(max_length=30,default='Null', blank=True)
    vatreg = models.CharField(max_length=30,default='Null', blank=True)
    vatregrc = models.CharField(max_length=30,default='Null', blank=True)
    vatregver = models.CharField(max_length=30,default='Null', blank=True)
    comreg = models.CharField(max_length=30,default='Null', blank=True)
    comregrc = models.CharField(max_length=30,default='Null', blank=True)
    comregver = models.CharField(max_length=30,default='Null', blank=True)
    dl = models.CharField(max_length=30,default='Null', blank=True)
    dlrc = models.CharField(max_length=30,default='Null', blank=True)
    dlver = models.CharField(max_length=30,default='Null', blank=True)
    od = models.CharField(max_length=30,default='Null', blank=True)
    odrc = models.CharField(max_length=30,default='Null', blank=True)
    odver = models.CharField(max_length=30,default='Null', blank=True)
    rfacf = models.CharField(max_length=30,default='Null', blank=True)
    tv = models.CharField(max_length=30,default='Null', blank=True)
    expdt = models.CharField(max_length=30,default='Null', blank=True)
    wpoa = models.CharField(max_length=30,default='Null', blank=True)
    cpep = models.CharField(max_length=30,default='Null', blank=True)
    abtsm = models.CharField(max_length=30,default='Null', blank=True)
    cbif = models.CharField(max_length=30,default='Null', blank=True)
    terr = models.CharField(max_length=30,default='Null', blank=True)
    iyterr = models.CharField(max_length=30,default='Null', blank=True)
    rg = models.CharField(max_length=30,default='Null', blank=True)
    cmnt = models.CharField(max_length=30,default='Null', blank=True)

    def _str_(self):
        return self.branch
