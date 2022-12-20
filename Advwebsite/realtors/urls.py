from django.urls import path
from . import views
app_name = "realtors"

urlpatterns=[
    path('login',views.login, name='login'),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout')

]

# In the dashboard realtors should be able to see all their listings as well as there should be an option to list new property for rent