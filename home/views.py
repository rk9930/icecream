from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout

from django.contrib.auth import authenticate, login
from home.models import Contact, Bookings
from django.contrib import messages
# Create your views here.
def index(request):
    return render (request, "index.htm")
def  about(request):
    return render (request, "about.htm")
    # return HttpResponse("This is about ")
def services(request):
    return render (request, "services.htm")
def icecream(request):
    return render (request, "icecream.htm")
def softy(request):
    return render (request, "softy.htm")
def familypack(request):
    return render (request, "familypack.htm")
    # return HttpResponse("This is services ")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        messages.success(request, 'Your message has been sent!')
    # return render(request, 'contact.html')
    return render (request, 'contact.htm')
    # return HttpResponse("This is contact")
def query(request):
    return render (request, "index.htm")
    # return HttpResponse("This is query")
def buy(request):
    if request.user.is_anonymous:
        return redirect("/login")
    elif request.method=="POST":
        name=request.POST.get('name')
        procode=request.POST.get('procode')
        username=request.POST.get('username')
        mnumber=request.POST.get('mnumber')
        address = request.POST.get('address')
        zipp=request.POST.get('zipp')
        pmode = request.POST.get('pmode')
        booking = Bookings(name= name, procode=procode, username=username, mnumber= mnumber, address=address, zipp=zipp, pmode=pmode)
        booking.save()

    return render(request, "buy.htm")
def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
            # A backend authenticated the credentials
        else:
            # No backend authenticated the credentials
            return render(request, "login.htm")
    return render(request, "login.htm")
def logoutUser(request):
    logout(request)
    return redirect("/login")
def register(request):
    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_2 = User.objects.create_user(username, email, password)
        user_2.save()
    return render(request, "register.htm")