from pyexpat.errors import messages

from django.shortcuts import render,redirect



def home_page(request):
    return render(request,'base.html')


