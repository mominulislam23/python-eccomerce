
from multiprocessing import context
from django.shortcuts import render, HttpResponse , redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from .models import Product
from math import ceil


# Create your views here.
def index(request):
    context = {

    "variable": "this is sent"
}
    
    return render(request, 'index.html', context)
    #return HttpResponse("this is home page")
def about(request):
      return render(request, 'about.html')
    #return HttpResponse("this is about page")
   
def contact(request):
      if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, phone = phone, email=email, desc=desc, date = datetime.today())
        contact.save() 
        messages.success(request, 'Your message has been sent!')
      return render(request, 'contact.html')
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request, 'Profile.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")




def profile(request):
      return render(request, 'profile.html')




def shop(request):
    products= Product.objects.all()
    allProds=[]
    catprods= Product.objects.values('category', 'id')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params={'allProds':allProds }
    return render(request,"shop.html", params)



def tracker(request):
      return render(request, 'shop.html')   




def productView(request, myid):

    # Fetch the product using the id
    products = Product.objects.filter(id=myid)
    return render(request, 'prodview.html', {'product':products[0]})

def checkout(request):
      return render(request, 'checkout.html')            