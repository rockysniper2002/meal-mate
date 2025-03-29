from django.shortcuts import render
from django.http import HttpResponse
from delivery.models import Customer, Restaurant
# Create your views here.

def index(request):
    return render(request,'delivery/index.html')

def signin(request):
    return render(request,'delivery/signin.html')

def signup(request):
    return render(request,'delivery/signup.html')

def handle_login(request):
    #DB Data
    # user = 'deep'
    # pw ='123'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # return HttpResponse(f"Username: {username} Password: {password}")
        # if username == user and  password == pw:

        try:
            cust = Customer.objects.get(username = username, password = password)
            return render(request,'delivery/success.html')
        except:
            return render(request,'delivery/failed.html')

    else:
        return HttpResponse(f"Invalid Username or Password")

def handle_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')

        try:
            cust = Customer.objects.get(username = username)
            # return render(request,'delivery/success.html')
        except:
            # return render(request,'delivery/failed.html')
            c = Customer(username = username, password = password, email = email, mobile = mobile, address = address) 
            c.save()

        return render(request,'delivery/signin.html')
        # data = {
        # "username": username, 
        # "password": password, 
        # "email": email, 
        # "mobile": mobile, 
        # "address": address
        # }

        # return render(request,'delivery/userdata.html',data)
         
    else:
        return HttpResponse(f"Invalid Request")

def restaurant_page(request):
    return render(request,'delivery/add_restaurant.html')

def add_restaurant(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        picture = request.POST.get('picture')
        cuisine = request.POST.get('cuisine')
        rating = request.POST.get('rating')

        rest = Restaurant(name = name, picture = picture, cuisine = cuisine, rating = rating)
        rest.save()
        
        restaurants = Restaurant.objects.all()

        return render(request,'delivery/show_restaurants.html',{"restaurants": restaurants})
        
         
    else:
        return HttpResponse(f"Invalid Request")
