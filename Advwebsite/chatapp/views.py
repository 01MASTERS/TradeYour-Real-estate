from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import Contacts
from django.http import HttpResponse

#tenant side
# called when user clicks on specific listing grp link after authentication
def tenant_joingrp(request):
    return HttpResponse('hello4')

# called after authentication
def tenant_chatwindow(request):
    return HttpResponse('hello5')

def tenant_leavegrp(request):
    return HttpResponse('hello4')

# owner side
def creategrp(request):
    pass

def register(request):
    pass

def owner_joingrp(request):
    return HttpResponse('hello4')

def owner_chatwindow(request):
    return HttpResponse('hello5')

def owner_leavegrp(request):
    return HttpResponse('hello4')