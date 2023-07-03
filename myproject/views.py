from django.shortcuts import render,redirect,HttpResponse
from app.emailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import CustomUser

def base(request):
    return render(request,'base.html')

def loginpage(request):
    return render(request, 'login.html')

def doLogin(request):
    if request.method == 'POST':
        user= EmailBackEnd.authenticate(request,
                                        username=request.POST.get('email'),
                                        password=request.POST.get('password'),)
        if user!=None:
            login(request, user)
            user_type= user.user_type
            if user_type == '1':
                return redirect('base')
            elif user_type == '2':
                return redirect('base')
        
            else:
                messages.error(request, 'Email or Password is invalid')
                return redirect('loginpage')
        else:
            messages.error(request, 'Email or Password is invalid')
            return redirect('loginpage')
        
def doLogout(request):
    logout(request)
    return redirect(loginpage)


