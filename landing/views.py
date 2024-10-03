from django.shortcuts import render,redirect
from .models import PreBooking
from django.contrib import messages

def LandingPage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        if name and email and phone:
            messages.success(request, "Congratulations on Pre-Booking!")
            PreBooking.objects.create(name=name, email=email, phone=phone)
            return redirect("landingpage")
        else:
            messages.error(request, "Please fill in all fields.")
        

    return render(request, "index.html")
