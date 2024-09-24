from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as log
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from user.form import LoanForm





def index(request):
    return render(request,'home.html')





def login(request):
    return render(request,'user/login.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']    
        
        user = authenticate(request,username=username, password=password)

        if user is not None:
            if user.is_superuser == 0:

                log(request,user)
                return redirect('/home')

            else:
                return redirect("/user/login")


        else:
            return redirect("/user/login")

    else:
            return redirect("/user/login")


def register(request):
    return render(request,'user/register.html')

# To register User

def register_user(request):
    if request.method == "POST":
        User.objects.create_user(
            first_name = request.POST['fullname'],
            username = request.POST['username'],
            password = request.POST['password'],
            email = request.POST['phonenumber'],

        )
        return redirect('/user/login')
    


    else:
        return render(request, '404.html', status=404)

def log_out(request):
    logout(request)
    return redirect('/home')

def contact(request):

    return render(request,'contact.html')

@login_required(login_url='/user/login')

def loan(request):
    return render(request, 'loan.html')


@login_required(login_url='/user/login')

def addloan(request):


    if request.method == 'POST':
        # Create a new LoanModel instance with the submitted data
        loan_instance = LoanForm(
            gender=request.POST.get('gender'),
            married=request.POST.get('married'),
            dependent=request.POST.get('dependent'),
            education=request.POST.get('education'),
            employment=request.POST.get('employment'),  # Make sure this field matches your model
            income=request.POST.get('income'),
            co_income=request.POST.get('co_income'),
            loan=request.POST.get('loan'),
            loan_term=request.POST.get('loan_term'),
            credit=request.POST.get('credit'),
            property_area=request.POST.get('property_area'),
            user_id=request.user  # Assuming you're associating the loan with the logged-in user
        )
        loan_instance.save() 
   
    return redirect('/index')



