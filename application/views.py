import math
from statistics import quantiles
from tokenize import Double
from django.shortcuts import render, redirect
from time import localtime, strftime
from .models import Order

# Display
def dispIndex(request):
    return render(request, "index.html")

def dispOnlineOrder(request):
    if 'order_cost' in request.session:
        context = {
            # 'order_details': request.session['order_details'],
            'sales_tax': request.session['sales_tax'],
            'order_total': request.session['order_total'],
            'order_dict': request.session['order_dict'],
            "date": strftime("%A, %B %d, %Y"),
            "time": strftime("%I:%M %p %Z",
            localtime())
        }
        request.session.save()
        return render(request, "online_order.html", context)
    else:
        context = {
            "date": strftime("%A, %B %d, %Y"),
            "time": strftime("%I:%M %p %Z",
            localtime())
        }
        request.session['order_cost'] = 0.0
        # request.session['order_details'] = []
        request.session['sales_tax'] = 0.0
        request.session['order_total'] = 0.0
        request.session['order_dict'] = {}
        return render(request, "online_order.html", context)

def dispComingSoon(request):
    return render(request, "page_coming_soon.html")

def dispGallery(request):
    return render(request, "gallery.html")

def checkout_success(request, order_id):
    if 'order_dict' in request.session:
        orderDictionary = request.session['order_dict']
        context = {
            "this_order": Order.objects.get(id=order_id),
            "order_dict": orderDictionary
        }
        request.session.clear()
        return render(request, "checkout.html", context)
    else:
        return redirect("/")

    # for testing:
    # orderDictionary = request.session['order_dict']
    # context = {
    #     "this_order": Order.objects.get(id=order_id),
    #     "order_dict": orderDictionary
    # }
    # return render(request, "checkout.html", context)

def add(request):
    if request.POST['food'] == "kotteri":
        # print(request.session["order_dict"])
        request.session["order_cost"] += int(request.POST['quantity']) * float(11.50);
        orderDictionary = request.session["order_dict"]
        # print(orderDictionary)
        if "Kotteri" in orderDictionary:
            current_quantity = orderDictionary["Kotteri"]
            orderDictionary["Kotteri"] = int(current_quantity) + int(request.POST["quantity"])
        else:
            orderDictionary["Kotteri"] = request.POST['quantity']
            request.session["order_dict"] = orderDictionary
        # print(orderDictionary)
        # print(request.session["order_dict"])
        # request.session["order_details"].append(f"Kotteri - Quantity {request.POST['quantity']}") 
    if request.POST['food'] == "mala_kotteri":
        request.session["order_cost"] += int(request.POST['quantity']) * float(12);
        orderDictionary = request.session["order_dict"]
        if "Mala Kotteri" in orderDictionary:
            current_quantity = orderDictionary["Mala Kotteri"]
            orderDictionary["Mala Kotteri"] = int(current_quantity) + int(request.POST["quantity"])
        else:
            orderDictionary["Mala Kotteri"] = request.POST['quantity']
            request.session["order_dict"] = orderDictionary
    if request.POST['food'] == "shio":
        request.session["order_cost"] += int(request.POST['quantity']) * float(11);
        orderDictionary = request.session["order_dict"]
        if "Shio" in orderDictionary:
            current_quantity = orderDictionary["Shio"]
            orderDictionary["Shio"] = int(current_quantity) + int(request.POST["quantity"])
        else:
            orderDictionary["Shio"] = request.POST['quantity']
            request.session["order_dict"] = orderDictionary
    if request.POST['food'] == "shoyu":
        request.session["order_cost"] += int(request.POST['quantity']) * float(11);
        orderDictionary = request.session["order_dict"]
        if "Shoyu" in orderDictionary:
            current_quantity = orderDictionary["Shoyu"]
            orderDictionary["Shoyu"] = int(current_quantity) + int(request.POST["quantity"])
        else:
            orderDictionary["Shoyu"] = request.POST['quantity']
            request.session["order_dict"] = orderDictionary 
    if request.POST['food'] == "spicy_vegetarian":
        request.session["order_cost"] += int(request.POST['quantity']) * float(12);
        orderDictionary = request.session["order_dict"]
        if "Spicy Vegetarian" in orderDictionary:
            current_quantity = orderDictionary["Spicy Vegetarian"]
            orderDictionary["Spicy Vegetarian"] = int(current_quantity) + int(request.POST["quantity"])
        else:
            orderDictionary["Spicy Vegetarian"] = request.POST['quantity']
            request.session["order_dict"] = orderDictionary
    if request.POST['food'] == "vegetarian_miso":
        request.session["order_cost"] += int(request.POST['quantity']) * float(11.50);
        orderDictionary = request.session["order_dict"]
        if "Vegetarian Miso" in orderDictionary:
            current_quantity = orderDictionary["Vegetarian Miso"]
            orderDictionary["Vegetarian Miso"] = int(current_quantity) + int(request.POST["quantity"])
        else:
            orderDictionary["Vegetarian Miso"] = request.POST['quantity']
            request.session["order_dict"] = orderDictionary
    if request.POST['food'] == "shanghai":
        request.session["order_cost"] += int(request.POST['quantity']) * float(6);
        orderDictionary = request.session["order_dict"]
        if "Shanghai" in orderDictionary:
            current_quantity = orderDictionary["Shanghai"]
            orderDictionary["Shanghai"] = int(current_quantity) + int(request.POST["quantity"])
        else:
            orderDictionary["Shanghai"] = request.POST['quantity']
            request.session["order_dict"] = orderDictionary
    if request.POST['food'] == "ayamgoreng":
        request.session["order_cost"] += int(request.POST['quantity']) * float(9);
        orderDictionary = request.session["order_dict"]
        if "Ayamgoreng" in orderDictionary:
            current_quantity = orderDictionary["Ayamgoreng"]
            orderDictionary["Ayamgoreng"] = int(current_quantity) + int(request.POST["quantity"])
        else:
            orderDictionary["Ayamgoreng"] = request.POST['quantity']
            request.session["order_dict"] = orderDictionary
    if request.POST['food'] == "chicken_sandwich":
        request.session["order_cost"] += int(request.POST['quantity']) * float(9);
        orderDictionary = request.session["order_dict"]
        if "Chicken Sandwich" in orderDictionary:
            current_quantity = orderDictionary["Chicken Sandwich"]
            orderDictionary["Chicken Sandwich"] = int(current_quantity) + int(request.POST["quantity"])
        else:
            orderDictionary["Chicken Sandwich"] = request.POST['quantity']
            request.session["order_dict"] = orderDictionary
    calculateTotal(request)
    # request.session['sales_tax'] = request.session['order_cost'] * .1025
    # order_total = request.session['order_cost'] + request.session['sales_tax']
    # request.session['order_total'] = format(order_total, ".2f")
    return redirect("/order")

def calculateTotal(request):
    request.session['sales_tax'] = request.session['order_cost'] * .1025
    order_total = request.session['order_cost'] + request.session['sales_tax']
    request.session['order_total'] = format(order_total, ".2f")
    # print(request.session['order_total'])

def increase_quantity(request, key):
    if key == "Kotteri":
        # print(request.session["order_dict"])
        request.session["order_cost"] += float(11.50);
        orderDictionary = request.session["order_dict"]
        # print(orderDictionary)
        quantity = int(orderDictionary["Kotteri"])
        quantity += 1;
        orderDictionary["Kotteri"] = quantity
        request.session["order_dict"] = orderDictionary
    if key == "Mala Kotteri":
        request.session["order_cost"] += float(12);
        orderDictionary = request.session["order_dict"]
        quantity = int(orderDictionary["Mala Kotteri"])
        quantity += 1;
        orderDictionary["Mala Kotteri"] = quantity
        request.session["order_dict"] = orderDictionary
    if key == "Shio":
        request.session["order_cost"] += float(11);
        orderDictionary = request.session["order_dict"]
        quantity = int(orderDictionary["Shio"])
        quantity += 1;
        orderDictionary["Shio"] = quantity
        request.session["order_dict"] = orderDictionary
    if key == "Shoyu":
        request.session["order_cost"] += float(11);
        orderDictionary = request.session["order_dict"]
        quantity = int(orderDictionary["Shoyu"])
        quantity += 1;
        orderDictionary["Shoyu"] = quantity
        request.session["order_dict"] = orderDictionary
    if key == "Spicy Vegetarian":
        request.session["order_cost"] += float(12);
        orderDictionary = request.session["order_dict"]
        quantity = int(orderDictionary["Spicy Vegetarian"])
        quantity += 1;
        orderDictionary["Spicy Vegetarian"] = quantity
        request.session["order_dict"] = orderDictionary
    if key == "Vegetarian Miso":
        request.session["order_cost"] += float(11.50);
        orderDictionary = request.session["order_dict"]
        quantity = int(orderDictionary["Vegetarian Miso"])
        quantity += 1;
        orderDictionary["Vegetarian Miso"] = quantity
        request.session["order_dict"] = orderDictionary
    if key == "Shanghai":
        request.session["order_cost"] += float(6);
        orderDictionary = request.session["order_dict"]
        quantity = int(orderDictionary["Shanghai"])
        quantity += 1;
        orderDictionary["Shanghai"] = quantity
        request.session["order_dict"] = orderDictionary
    if key == "Ayamgoreng":
        request.session["order_cost"] += float(9);
        orderDictionary = request.session["order_dict"]
        quantity = int(orderDictionary["Ayamgoreng"])
        quantity += 1;
        orderDictionary["Ayamgoreng"] = quantity
        request.session["order_dict"] = orderDictionary
    if key == "Chicken Sandwich":
        request.session["order_cost"] += float(9);
        orderDictionary = request.session["order_dict"]
        quantity = int(orderDictionary["Chicken Sandwich"])
        quantity += 1;
        orderDictionary["Chicken Sandwich"] = quantity
        request.session["order_dict"] = orderDictionary
    calculateTotal(request)
    return redirect("/order");

def decrease_quantity(request, key):
    if key == "Kotteri":
        # print(request.session["order_dict"])
        request.session["order_cost"] -= float(11.50);
        orderDictionary = request.session["order_dict"]
        # print(orderDictionary)
        quantity = int(orderDictionary["Kotteri"])
        quantity -= 1;
        if quantity == 0:
            orderDictionary.pop("Kotteri")
        else:
            orderDictionary["Kotteri"] = quantity
        request.session["order_dict"] = orderDictionary
    if key == "Mala Kotteri":
        request.session["order_cost"] -= float(12);
        orderDictionary = request.session["order_dict"]
        quantity = int(orderDictionary["Mala Kotteri"])
        quantity -= 1;
        if quantity == 0:
            orderDictionary.pop("Mala Kotteri")
        else:
            orderDictionary["Mala Kotteri"] = quantity
        request.session["order_dict"] = orderDictionary
    if key == "Shio":
        request.session["order_cost"] -= float(11);
        orderDictionary = request.session["order_dict"]
        quantity = int(orderDictionary["Shio"])
        quantity -= 1;
        if quantity == 0:
            orderDictionary.pop("Shio")
        else:
            orderDictionary["Shio"] = quantity
        request.session["order_dict"] = orderDictionary
    if key == "Shoyu":
        request.session["order_cost"] -= float(11);
        orderDictionary = request.session["order_dict"]
        quantity = int(orderDictionary["Shoyu"])
        quantity -= 1;
        if quantity == 0:
            orderDictionary.pop("Shoyu")
        else:
            orderDictionary["Shoyu"] = quantity
        request.session["order_dict"] = orderDictionary
    if key == "Spicy Vegetarian":
        request.session["order_cost"] -= float(12);
        orderDictionary = request.session["order_dict"]
        quantity = int(orderDictionary["Spicy Vegetarian"])
        quantity -= 1;
        if quantity == 0:
            orderDictionary.pop("Spicy Vegetarian")
        else:
            orderDictionary["Spicy Vegetarian"] = quantity
        request.session["order_dict"] = orderDictionary
    if key == "Vegetarian Miso":
        request.session["order_cost"] -= float(11.50);
        orderDictionary = request.session["order_dict"]
        quantity = int(orderDictionary["Vegetarian Miso"])
        quantity -= 1;
        if quantity == 0:
            orderDictionary.pop("Vegetarian Miso")
        else:
            orderDictionary["Vegetarian Miso"] = quantity
        request.session["order_dict"] = orderDictionary
    if key == "Shanghai":
        request.session["order_cost"] -= float(6);
        orderDictionary = request.session["order_dict"]
        quantity = int(orderDictionary["Shanghai"])
        quantity -= 1;
        if quantity == 0:
            orderDictionary.pop("Shanghai")
        else:
            orderDictionary["Shanghai"] = quantity
        request.session["order_dict"] = orderDictionary
    if key == "Ayamgoreng":
        request.session["order_cost"] -= float(9);
        orderDictionary = request.session["order_dict"]
        quantity = int(orderDictionary["Ayamgoreng"])
        quantity -= 1;
        if quantity == 0:
            orderDictionary.pop("Ayamgoreng")
        else:
            orderDictionary["Ayamgoreng"] = quantity
        request.session["order_dict"] = orderDictionary
    if key == "Chicken Sandwich":
        request.session["order_cost"] -= float(9);
        orderDictionary = request.session["order_dict"]
        quantity = int(orderDictionary["Chicken Sandwich"])
        quantity -= 1;
        if quantity == 0:
            orderDictionary.pop("Chicken Sandwich")
        else:
            orderDictionary["Chicken Sandwich"] = quantity
        request.session["order_dict"] = orderDictionary
    calculateTotal(request)
    return redirect("/order")

def clear(request):
    request.session.clear()
    return redirect("/order")

def checkout(request):
    orderDictionary = request.session['order_dict']
    total_quantity = 0
    for key, value in orderDictionary.items():
        total_quantity += int(value)
    new_order = Order.objects.create(
        quantity_ordered = total_quantity,
        subtotal = request.session['order_cost'],
        sales_tax = request.session['sales_tax'],
        total_cost = request.session['order_total'],
        itemized_order = request.session['order_dict']
    )
    print(new_order)
    return redirect(f"/success/{new_order.id}")