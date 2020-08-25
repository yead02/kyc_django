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
        toa = request.POST["toa"]
        cusocc = request.POST["cusocc"]
        cuspro = request.POST["cuspro"]
        sof = request.POST["sof"]
        doccol1 = request.POST["doccol1"]
        doccol2 = request.POST["doccol2"]
        doccol3 = request.POST["doccol3"]
        coldocver = request.POST["coldocver"]
        addaccver = request.POST["addaccver"]
        benownacc = request.POST["benownacc"]
        passno = request.POST["passno"]
        passnorc = request.POST["passnorc"]
        passnover = request.POST.get("passnover")
        nid = request.POST["nid"]
        nidrc = request.POST.get("nidrc")
        nidver = request.POST.get("nidver")
        etin = request.POST["etin"]
        etinrc = request.POST.get("etinrc")
        etinver = request.POST.get("etinver")
        bcer = request.POST["bcer"]
        bcerrc = request.POST.get("bcerrc")
        bcerver = request.POST.get("bcerver")
        vatreg = request.POST["vatreg"]
        vatregrc = request.POST.get("vatregrc")
        vatregver = request.POST.get("vatregver")
        comreg = request.POST["comreg"]
        comregrc = request.POST.get("comregrc")
        comregver = request.POST.get("comregver")
        dl = request.POST["dl"]
        dlrc = request.POST.get("dlrc")
        dlver = request.POST.get("dlver")
        od = request.POST["od"]
        odrc = request.POST.get("odrc")
        odver = request.POST.get("odver")
        rfacf = request.POST.get("rfacf")
        tv = request.POST["tv"]
        expdt = request.POST["expdt"]
        wpoa = request.POST.get("wpoa")
        cpep = request.POST["cpep"]
        abtsm = request.POST.get("abtsm")
        cbif = request.POST.get("cbif")
        terr = request.POST["terr"]
        iyterr = request.POST["iyterr"]
        rg = request.POST["rg"]
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
