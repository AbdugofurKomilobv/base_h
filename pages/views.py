from django.contrib.auth import logout
from django.shortcuts import render, redirect
from user_app.models import User
from django.db.utils import IntegrityError


def home_page(request):
    return render(request,'base.html')





