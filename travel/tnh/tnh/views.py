from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    
    return render (request,"Hotel.html")

def Loginpage(request):
    return render (request,"login.html")

def beaches(request):
    return render(request, "templates/beaches.html")

def about_us(request):
    return render(request, "templates/navbar/about_us.html")

def contact(request):
    return render(request, "templates/navbar/contact.html")

def logout(request):
    return render(request, "templates/navbar/logout.html")

def profile(request):
    return render(request, "templates/navbar/profile.html")



