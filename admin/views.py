import re
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as log
from django.contrib.auth import logout




# Create your views here.


def login(request):
    return render(request,'admin/login.html')

@login_required(login_url='/admin')
def index(request):
    return render(request,'admin/adminindex.html')

def login_superuser(request):

        username= request.POST['username']
        password= request.POST['password']

        user = authenticate(request,username=username, password=password)

        
        if user is not None:
            log(request,user)

            if user.is_superuser == 1:

                return redirect('/admin/home')

            else:
                return redirect('/admin')

        else:
            return redirect('/admin')
    
def log_out(request):
    logout(request)
    return redirect('/admin')

@login_required(login_url='/admin')
def details(request):
    user=User.objects.all()
    return render(request,'admin/admindetails.html',{'user':user})

@login_required(login_url='/admin')
def delete_user(request,id):
    user=User.objects.get(id=id)
    user.delete()
    user=User.objects.all()
    return render(request,'admin/admindetails.html',{'user':user})
