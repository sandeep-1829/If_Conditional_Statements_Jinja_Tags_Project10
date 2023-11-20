from django.shortcuts import render

# Create your views here.

def conditions(request):
    Dict={'a':10000,'b':20000,'c':50000}
    return render(request,'conditions.html',Dict)
