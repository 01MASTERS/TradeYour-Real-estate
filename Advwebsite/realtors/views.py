from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import Contacts
from realtors.models import Realtor

def register(request):
    if request.method=='POST':
        # Username, password, Name, Photo, Phone for register

        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        photo = request.POST['photo']


        if password==password2:
            if Realtor.objects.filter(username=username).exists():
                messages.error(request,'Username already exists')
                return redirect('realtors:register')
            else:
                if Realtor.objects.filter(email=email).exists():
                    messages.error(request, 'email already registered ')
                    return redirect('realtors:register')
                else:
                    realtor = Realtor.objects.create(username=username, password=password, name=name,
                                               email=email, phone=phone, photo=photo)
                    realtor.save()
                    messages.success(request, 'You are successfully registered')
                    return redirect('realtors:login')

        else:
            messages.error(request, 'Passwords do not match')
            return redirect('realtors:register')

    else:
        return render(request, "realtors/register.html")

def login(request):

    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password= password)

        if user is not None :
            auth.login(request , user )
            messages.success(request, 'You are succesfully logged in')
            return redirect('accounts:dashboard')
        else:
            messages.error(request, 'User does not exist')
            return redirect('accounts:login')

    else:
       return render(request, "realtors/login.html")

def logout(request):
      messages.success(request, 'You have successfully logged out')
      auth.logout(request)
      return redirect('pages:index2')

def dashboard(request):
    contacts = Contacts.objects.filter(user_id=request.user.id)
    contt={'contacts' : contacts}
    return render(request, "realtors/dashboard.html", contt)
