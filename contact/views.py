from django.shortcuts import render
from .models import contact

# Create your views here.
def contactus(request):
    if request.method == 'POST':
        contactdata=contact()
        contactdata.name=request.POST.get('name')
        contactdata.email=request.POST.get('email')
        contactdata.subject=request.POST.get('subject')
        contactdata.message=request.POST.get('message')
        contactdata.save()
    return render(request,'contact.html')
