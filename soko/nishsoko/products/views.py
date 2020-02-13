from django.http import request
from django.shortcuts import render, get_object_or_404
from .models import AddProduct
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    obj = AddProduct.objects.all()

    return render(request,"index.html",{"object":obj})

def product(request, id):
    obj=AddProduct.objects.get(id=id)

    return render(request,"product.html",{"object1":obj})

def search(request):
    if request.method == "GET":
        q=request.GET.get('q')
        result=AddProduct.objects.filter(title__icontains=q)
        if not result:
            messages.info(request, "None of the product matches the word "+q)

    return render(request, "search.html", {"search":result})
'''
def add_to_cart(reguest, id ):
    item = get_object_or_404(AddProduct, id=id )
    order_item = OrderItem.objects.create(item=item)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exist():
        order = order_qs[0]
        if order.items.filter(item_id =item.id).exists():
            order_item.quantity +=1
            order_item.save()
    else:
        order = Order.objects.create(user=request.user)
        order.items.add(order_item)
    return render(request, "cart.html")

def add_to_cart(request, id):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.id).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("index")
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("index")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("index")
        '''