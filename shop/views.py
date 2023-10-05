from django.shortcuts import render
from .models import *
from math import *
import json
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    topDeal = TopDeal.objects.all()
    allProds = []
    catProds = Product.objects.values("category", "id")
    cats = {item["category"] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {"allProds": allProds, "topDeal": topDeal}
    return render(request, "index.html", params)


def searchMatch(query, item):
    if (
        query in item.product_desc.lower()
        or query in item.product_name.lower()
        or query in item.category.lower()
    ):
        return True
    else:
        return False


def search(request):
    query = request.GET.get("search")
    topDeal = TopDeal.objects.all()
    allProds = []
    catProds = Product.objects.values("category", "id")
    cats = {item["category"] for item in catProds}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
            topDeal = []
        else:
            topDeal = []

    params = {"allProds": allProds, "topDeal": topDeal, "mssg": ""}
    if len(allProds) == 0:
        params = {"mssg": "No Product according to your search!"}
    return render(request, "search.html", params)


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        mssg = request.POST.get("mssg")
        contact = Contact(name=name, phone=phone, email=email, mssg=mssg)
        contact.save()

        thank = True
        return render(request, "contact.html", {"thank": thank})
    return render(request, "contact.html")

@login_required(login_url='signin')
def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get("itemsJson")
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        amount = request.POST.get("amount")
        address = request.POST.get("address")
        zip_code = request.POST.get("zip_code")
        city = request.POST.get("city")
        state = request.POST.get("state")
        mssg = request.POST.get("mssg")

        order = Orders(
            name=name,
            phone=phone,
            email=email,
            mssg=mssg,
            address=address,
            zip_code=zip_code,
            city=city,
            state=state,
            items_json=items_json,
            amount=amount,
        )
        order.save()
        update = OrderUpdate(
            order_id=order.order_id, update_desc="The order has been placed."
        )
        update.save()
        thank = True
        id = order.order_id
        return render(request, "checkout.html", {"thank": thank, "id": id})

    return render(request, "checkout.html")


def tracker(request):
    if request.method == "POST":
        orderid = request.POST.get("orderid")
        email = request.POST.get("email")
        try:
            order = Orders.objects.filter(order_id=orderid, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderid)
                updates = []
                for item in update:
                    updates.append({"text": item.update_desc, "time": item.timestamp})
                    response = json.dumps(
                        {
                            "status": "success",
                            "updates": updates,
                            "itemsJson": order[0].items_json,
                        },
                        default=str,
                    )
                return HttpResponse(response)
            else:
                return HttpResponse('{"status": "noitem"}')
        except Exception as e:
            return HttpResponse('{"status": "error"}')

    return render(request, "tracker.html")


def productView(request, myid):
    product = Product.objects.filter(id=myid)
    return render(request, "prodView.html", {"product": product[0]})


def dealsView(request, myid):
    deals = TopDeal.objects.filter(id=myid)
    return render(request, "dealsView.html", {"deals": deals[0]})


def signup(request):
    # Signup
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        ConfirmPassword = request.POST.get('password2')

        if  len(name) < 4:
            messages.error(request, "Name must be atleast 4 Characters")
            return redirect('signup')

        if password != ConfirmPassword:
            messages.error(request, "Password and Confirm Password is not match.")
            return redirect('signup')
        else: 
            reg_data = User.objects.create_user(first_name=name, username=email, password=password)
            reg_data.save()
            messages.success(request, "Your account has been created.")
            return redirect('signin')
    
    return render(request, 'signup.html')

def signin(request):
    # Signin
    if request.method == 'POST':
        Email = request.POST['email']
        Password = request.POST['password']

        user=authenticate(username=Email, password=Password)

        if user is not None:
            login(request,user) 
            return redirect('/')
        else:
            messages.error(request, "Email or Password is incorrect!")
            return redirect('signin')
        
    return render(request, "signin.html")

def signout(request):
    messages.success(request, "You Have Been Signout!")
    logout(request)
    return redirect('home')


def about(request):
    return render(request, "about.html")


def pre_build(request):
    return render(request, "pre-build.html")


def laptops(request):
    return render(request, "laptops.html")


def subscription(request):
    return render(request, "subscription.html")
