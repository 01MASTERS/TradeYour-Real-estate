from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import Contacts
from realtors.models import Realtor
from listings.models import Listing
from .choices import price_choices, bedroom_choices , bathroom_choices, city_choices, state_choices

def register(request):
    if request.method=='POST':
        # Username, password, Name, Photo, Phone for register

        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        photo = request.FILES.get('photo')


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
            return redirect('realtors:dashboard')
        else:
            messages.error(request, 'User does not exist')
            return redirect('accounts:login')

    else:
       return render(request, "realtors/login.html")

def logout(request):
      messages.success(request, 'You have successfully logged out')
      auth.logout(request)
      return redirect('pages:choice')

def dashboard(request):
    realtor = request.user
    listings = Listing.objects.filter(realtor=realtor)
    contt={'listings' : listings}
    return render(request, "realtors/dashboard.html", contt)

# realtor, title, address, city, state, zipcode, description, price, bedrooms, bathrooms, garage, sqft, lot_size, photo_main, photo_1, photo_2, list_date, is_published
def list(request):
    if request.method=='POST':
        realtor = request.user
        title = request.POST['title']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        description = request.POST['description']
        price = request.POST['price']
        bedrooms = request.POST['bedrooms']
        bathrooms = request.POST['bathrooms']
        garage = request.POST['garage']
        sqft = request.POST['sqft']
        lot_size = request.POST['lot_size']
        photo_main = request.FILES.get('photo_main')
        photo_1 = request.FILES.get('photo_1')
        photo_2 = request.FILES.get('photo_2')
               
        listing = Listing.objects.create(realtor = realtor, title=title, address = address , city = city,
                                state = state, zipcode = zipcode, description = description, price = price,
                                bedrooms = bedrooms, bathrooms = bathrooms, garage = garage, sqft = sqft, lot_size = lot_size,
                                photo_main = photo_main, photo_1 = photo_1, photo_2 = photo_2)
        listing.save()
        messages.success(request, 'You have successfully listed a listing')
        return redirect('realtors:dashboard')

    else:
        contt={
           'bedroom_choices':bedroom_choices,
           'bathroom_choices': bathroom_choices,
           'city_choices': city_choices,
           'state_choices': state_choices}
        return render(request, 'realtors/list.html', contt)
