from django.urls import path
from . import views
app_name="listings"

urlpatterns=[
    path('',views.index, name='index'),                       #We will see all the listings from here
    path('<int:listing_id>', views.listing, name='listing'),  #Tenant will see specific listings from here
    path('listing_for_realtor/<int:listing_id>', views.listing_for_realtor, name='listing_for_realtor'), # Realtor will see specific listings from here
    path('search', views.search, name='search'),
    
]