from django.shortcuts import render, HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices , bathroom_choices, city_choices, state_choices
from django.contrib import messages,auth

def choice(request):
    auth.logout(request)
    if request.method =='POST':
        user = request.POST['user']
        
        if(user == "tenant"):
            return render(request, "accounts/login.html")

        elif(user == "realtor"):
            return render(request, "realtors/login.html")
    else:
        return render(request, 'pages/choice.html')



def tenant_index(request):
    listingslt=Listing.objects.order_by('-list_date').filter(is_published=True)
    contt = {'listingslt':listingslt,
           'price_choices':price_choices,
           'bedroom_choices':bedroom_choices,
           'bathroom_choices': bathroom_choices,
           'city_choices': city_choices,
           'state_choices': state_choices}
    return render(request, 'pages/index.html', contt)

def realtor_index(request):
    return render(request, 'pages/index2.html')

def about_tenant(request):
    return render(request, 'pages/about.html')


def about_realtor(request):
    return render(request, 'pages/about2.html')

def about_project(request):
    return render(request, 'pages/about3.html')


