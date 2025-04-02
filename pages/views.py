from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from user_app.forms import MessageForm
from user_app.models import User,Message
from django.db.utils import IntegrityError


def home_page(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({"success": True})  # AJAX so‘rovlari uchun
            messages.success(request, "Xabaringiz yuborildi!")
            return render(request,'base.html')
    else:
        form = MessageForm()

    return render(request,'base.html',{"form":form})





