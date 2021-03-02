from django.shortcuts import render,redirect

from .models import isianKTP
from .form import tampilanformulir

def dashboard (request):
    return render(request,"registrasiKTP/dashboard.html")

def pengisianform (request):
    if request.method == "GET":
        kerangka_form={'form':tampilanformulir()}
        return render(request,"registrasiKTP/pengisianform.html",kerangka_form)
    else:
        form=tampilanformulir(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('/tampilan')
        else:
            return render(request,'registrasiKTP/pengisianform.html',{'form':form})
def tampilan(request):
    konten_tampilan={'isianKTP':isianKTP.objects.all}
    return render(request,"registrasiKTP/tampilan.html",konten_tampilan )