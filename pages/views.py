from django.shortcuts import render,redirect

from .models import Contact

def home_page(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        text = request.POST.get('text')

        Contact.objects.create(name=name,email=email,subject=subject,text=text)
        return redirect('home')


    return render(request,'base.html')
