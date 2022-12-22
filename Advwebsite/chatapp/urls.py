from django.urls import path
from . import views
app_name="chatapp"

urlpatterns=[
    path('creategrp', views.creategrp, name='creategrp'),
    path('register', views.register, name='register'),
    path('owner_joingrp', views.owner_joingrp, name='owner_joingrp'),
    path('owner_chatwindow', views.owner_chatwindow, name='owner_chatwindow'),
    path('owner_leavegrp', views.owner_leavegrp, name='owner_leavegrp'),
    path('tenant_joingrp', views.tenant_joingrp, name='tenant_joingrp'),
    path('tenant_chatwindow', views.tenant_chatwindow, name='tenant_chatwindow'),
    path('tenant_leavegrp', views.tenant_leavegrp, name='tenant_leavegrp')
]