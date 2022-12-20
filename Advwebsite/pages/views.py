from django.shortcuts import render, HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices , bathroom_choices, city_choices, state_choices


def choice(request):
    if request.method =='POST':
        realtor = request.POST['realtor?']
        tenant = request.POST['tenant?']
        if(realtor =="no" and tenant =="yes"):
            listingslt = Listing.objects.order_by('-list_date').filter(is_published=True)
            contt = {'listingslt': listingslt,
                     'price_choices': price_choices,
                     'bedroom_choices': bedroom_choices,
                     'bathroom_choices': bathroom_choices,
                     'city_choices': city_choices,
                     'state_choices': state_choices}
            return render(request, 'pages/index.html', contt)

        elif (realtor == "yes" and tenant == "no"):
            return render(request, 'pages/index2.html')
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
    realtors=Realtor.objects.all().order_by('-hire_date')
    contt = {'realtors': realtors}
    return render(request, 'pages/about.html', contt)


def about_realtor(request):
    realtors=Realtor.objects.all().order_by('-hire_date')
    contt = {'realtors': realtors}
    return render(request, 'pages/about2.html', contt)


