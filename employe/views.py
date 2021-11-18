from django.shortcuts import render
from django.http import HttpResponse

def employe(request):
    return HttpResponse("This is employee page")


def profile(request):
    return render(request,'employe/profile.html')



