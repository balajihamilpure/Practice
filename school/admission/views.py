from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import contact_form
# Create your views here.

def index(r):
    form = contact_form
    if r.method == 'POST':
        form = contact_form(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    context = {'form': form}
    return render(r,'index.html',context)

def contact(r):
    form=contact_form
    if r.method=='POST':
        form=contact_form(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    context={'form':form}
    return render(r,'contact1.html',context)

def about(r):
    return render(r,'test.html')

def admission(r):
    return render(r,'admission1.html')

def why(r):
    return render(r,'why1.html')