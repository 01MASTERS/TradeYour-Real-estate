"""Advwebsite URL Configuration cd

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls'), name='pages'),
    path('listings/', include('listings.urls'), name='listings'),
    path('contacts/', include('contacts.urls'), name='contacts'),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('realtors/', include('realtors.urls'), name='realtors'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# The /realtors/ path is for realtor login and signup
# in realtors app we have already created the realtor model and now we have to create views for realtors

# The /accounts/ path is for tenant login and signup
# in accounts app, we have already created views for tenants , and we dont need to create model for tenants as we are using Django ibuilt model aka "User" for tenants

