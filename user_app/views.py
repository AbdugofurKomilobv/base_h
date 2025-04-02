from django.contrib.auth import logout, authenticate, login
from django.db.utils import IntegrityError

from django.shortcuts import render, redirect
from .models import User


def register_page(request):
    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        phone_number = request.POST.get('phone_number', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')

        if not (name and phone_number and email and password):
            return render(request, 'register.html', {'error': "Barcha maydonlar to'ldirilishi kerak!"})


        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': "Bu email allaqachon ishlatilgan!"})
        if User.objects.filter(phone_number=phone_number).exists():
            return render(request, 'register.html', {'error': "Bu telefon raqam allaqachon ishlatilgan!"})

        try:
            user = User.objects.create_user(name=name, phone_number=phone_number, email=email, password=password)
            return redirect("pages:home")
        except IntegrityError:
            return render(request, 'register.html', {'error': "Ma'lumotlar bazasida xatolik yuz berdi!"})

    return render(request, 'register.html')




def login_page(request):
    if request.method == "POST":
        phone_number = request.POST.get('phone_number','').strip()
        password = request.POST.get('password','')

        if not (phone_number and password):
            return render(request,'login.html',{'error': "Tel num va parol kiritish zarur"})
        user = authenticate(request,phone_number=phone_number,password=password)
        print(f"User: {user}")

        if user is not None:
            login(request,user)
            return redirect("pages:home")
        else:
            return render(request,'login.html',{'error': "Tel num yoki parol xato"})
    return render(request,'login.html')




def logout_view(request):
    logout(request)
    return redirect('pages:home')