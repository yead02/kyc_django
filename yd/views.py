from django.shortcuts import render
from .models import fxd
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'index.html')


def gov(request):
    return render(request, 'Govt_Acc.html')


def fixd(request):
    return render(request, 'Fixed_Deposit.html')


def ind(request):
    return render(request, 'Individual.html')


def nind(request):
    return render(request, 'non-individual.html')


def fxd_add(request):
    if request.method == 'POST':
        branch = request.POST["branch"]
        date = request.POST["date"]
        acc_title = request.POST["acc_title"]
        toa = request.POST.get("toa",0)
        cusocc = request.POST["cusocc"]
        cuspro = request.POST["cuspro"]
        sof = request.POST["sof"]
        doccol1 = request.POST["doccol1"]
        doccol2 = request.POST["doccol2"]
        doccol3 = request.POST["doccol3"]
        coldocver = request.POST.get("coldocver",0)
        addaccver = request.POST["addaccver"]
        benownacc = request.POST.get("benownacc",0)
        passno = request.POST["passno"]
        passnorc = request.POST.get('passnorc',0)
        passnover = request.POST.get('passnover',0)
        nid = request.POST["nid"]
        nidrc = request.POST.get("nidrc",0)
        nidver = request.POST.get("nidver",0)
        etin = request.POST["etin"]
        etinrc = request.POST.get("etinrc",0)
        etinver = request.POST.get("etinver",0)
        bcer = request.POST["bcer"]
        bcerrc = request.POST.get("bcerrc",0)
        bcerver = request.POST.get("bcerver",0)
        vatreg = request.POST["vatreg"]
        vatregrc = request.POST.get("vatregrc",0)
        vatregver = request.POST.get("vatregver",0)
        comreg = request.POST["comreg"]
        comregrc = request.POST.get("comregrc",0)
        comregver = request.POST.get("comregver",0)
        dl = request.POST["dl"]
        dlrc = request.POST.get("dlrc",0)
        dlver = request.POST.get("dlver",0)
        od = request.POST["od"]
        odrc = request.POST.get("odrc",0)
        odver = request.POST.get("odver",0)
        rfacf = request.POST.get("rfacf",0)
        tv = request.POST["tv"]
        expdt = request.POST["expdt"]
        wpoa = request.POST.get("wpoa",0)
        cpep = request.POST.get("cpep",0)
        abtsm = request.POST.get("abtsm",0)
        cbif = request.POST.get("cbif",0)
        terr = request.POST.get("terr",0)
        iyterr = request.POST.get("iyterr",0)
        rg = request.POST.get("rg",0)
        cmnt = request.POST["cmnt"]

        fxxd = fxd(branch=branch, date=date, acc_title=acc_title, toa=toa, cusocc=cusocc, cuspro=cuspro, sof=sof,
               doccol1=doccol1, doccol2=doccol2, doccol3=doccol3, coldocver=coldocver, addaccver=addaccver,
               benownacc=benownacc, passno=passno, passnorc=passnorc, passnover=passnover,
               nid=nid, nidrc=nidrc, nidver=nidver, etin=etin, etinrc=etinrc, etinver=etinver, bcer=bcer, bcerrc=bcerrc,
               bcerver=bcerver, vatreg=vatreg, vatregrc=vatregrc, vatregver=vatregver, comreg=comreg, comregrc=comregrc,
               comregver=comregver, dl=dl, dlrc=dlrc, dlver=dlver,
               od=od, odrc=odrc, odver=odver, rfacf=rfacf, tv=tv, expdt=expdt, wpoa=wpoa, cpep=cpep, abtsm=abtsm,
               cbif=cbif, terr=terr, iyterr=iyterr, rg=rg, cmnt=cmnt)
        fxxd.save()

        return render(request, 'index.html')
