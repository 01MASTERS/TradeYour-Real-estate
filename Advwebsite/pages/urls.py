from django.urls import path
from . import views
app_name="pages"

urlpatterns=[
    path('', views.choice, name='choice'),
    path('user', views.tenant_index, name='index'),
    path('realtor', views.realtor_index, name='index2'),
    path('about', views.about_tenant, name='about'),
    path('about2', views.about_realtor, name='about2'),
    path('about3', views.about_project, name='about3')

]

# As soon as the user lands on our website
# i)  /  -> shows Are You a Looking for rent or Do you wanna list your property
# ii) /user -> for those who rea looking for  a rent
# iii) / realtor -> for those who wanna list their property
