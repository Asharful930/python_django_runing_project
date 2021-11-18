from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def login_page(request):
    if request.method=='POST':
        name = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
             messages.success(request, 'Form submission sdnxjvh')
    return render(request,'login.html')

def forgot_page(request):
    return render(request,'forgot.html')

def regstions_page(request):
    return render(request,'regstions.html')