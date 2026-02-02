from django.shortcuts import render,redirect

from products.models import *
from .models import *
from django.contrib import messages

from .forms import OrderForm

from django.contrib.auth.decorators import login_required

from django.urls import reverse


# Create your views here.



def homepage(request):
    # return HttpResponse("this is first app.")
        # 'products': Products.objects.filter(trending = True).order_by('-id')[:2]
    context = {
        'products': Products.objects.filter(trending = True).order_by('-id')
    }

    return render(request,'mainpage/index.html',context)

def userProducts(request):
    category = Category.objects.all()
    category_id = request.GET.get('category')

    if category_id:
        products = Products.objects.filter(category_id = category_id).order_by('-id')
    else:
        products = Products.objects.all().order_by('-id')

    context ={
        'products': products,
        'category': category,
        'selected_category': int(category_id) if category_id else None

    }
    return render(request,'mainpage/products.html',context)

def productDetails(request, product_id):
    product = Products.objects.get(id = product_id)
    context ={
        'product': product
    }
    return render(request,'mainpage/product_details.html',context)


@login_required
def addToCart(request, product_id):
    product = Products.objects.get(id=product_id)
    user = request.user

    existingItem = Cart.objects.filter(user = user, products = product) # left database
    if existingItem:
        messages.error(request,'Item Already Exists in a cart !')
        return redirect('userpage:product-details', product_id)
    else:
        Cart.objects.create(user = user , products = product) # could be done sames as passing instance = id
        messages.success(request,'item added to the cart')
        return redirect('userpage:all-products')


@login_required
def userCart(request):
    user = request.user
    cartitems = Cart.objects.filter(user = user)
    return render(request,'mainpage/cart.html',{'items':cartitems})

@login_required
def deleteCart(request,cart_id):
    cart_item = Cart.objects.get(id = cart_id)
    cart_item.delete()
    messages.success(request,'items removed successfully')
    return redirect('cart')


def orderForm(request,cart_id,product_id):
    cart = Cart.objects.get(id = cart_id)
    product = Products.objects.get(id = product_id)
    user = request.user

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            quantity = request.POST.get("quantity")
            price = product.selling_price
            total_price = int(price) * int(quantity)
            phone_no = request.POST.get("phone_no")
            address = request.POST.get("address")
            payment_method = request.POST.get('payment_method')
            

            order = Order.objects.create(

                user = user,
                product = product,
                quantity = quantity,
                total_price = total_price,
                phone_no = phone_no,
                address = address,
                payment_method = payment_method,
                payment_status = False,
            )

            if order.payment_method == 'CASH':
                cart = Cart.objects.get(id = cart_id)  # to delete from cart
                cart.delete()
                messages.success(request,"Order placed succesfully!!")
                return redirect('userpage:cart')
            elif order.payment_method == 'CARD':
                return redirect(reverse('stripe-checkout')+'?o_id='+ str(order.id)+'&c_id='+ str(cart.id) )
            else:
                messages.error(request,'Payemnt Failed')
                return redirect('userpage:cart')
        else:
            messages.error(request,'Form Invalid')
            return redirect('userpage:cart')


    context = {
        'orderform': OrderForm()
    }
    return render(request,'mainpage/order_form.html',context)


@login_required
def stripeCheckout(request):
    cart_id = request.GET.get('c_id')
    order_id = request.GET.get('o_id')
    cart = Cart.objects.get(id = cart_id)
    order = Order.objects.get(id = order_id)

    context = {
        'cart': cart,
        'order': order,
    }
    return render(request,'mainpage/checkout.html',context)

#! /usr/bin/env python3.6



import os
import stripe
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")



YOUR_DOMAIN = 'http://127.0.0.1:8000'

@login_required
def create_checkout_session(request,order_id,cart_id):
        order = Order.objects.get(id = order_id)
        cart = Cart.objects.get(id = cart_id)
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    # Provide the exact Price ID (for example, price_1234) of the product you want to sell
                    'price_data': {
                        'currency': 'NPR',
                        'product_data':{
                            'name': f"{order.product.name}"
                        },
                        'unit_amount': int(order.total_price) * 100
                    },
                    'quantity': order.quantity,
                },
            ],
            mode='payment',

            metadata = {
                'order_id': str(order.id),
                'cart_id': str(cart.id)
            },
            success_url=YOUR_DOMAIN + f'/success/?session_id={{CHECKOUT_SESSION_ID}}&order_id={order.id}&cart_id={cart.id}',
            cancel_url=YOUR_DOMAIN + '/cart',
        )
    
        return redirect(checkout_session.url, code=303)


def stripeSuccess(request):
    session_id = request.GET.get('session_id')
    order_id = request.GET.get('order_id')
    cart_id = request.GET.get('cart_id')

    if session_id:
        session = stripe.checkout.Session.retrieve(session_id)
        if session.payment_status == 'paid':
            order = Order.objects.get(id = order_id)
            cart = Cart.objects.get(id = cart_id)
            order.payment_status = True
            order.save()
            cart.delete()

            messages.success(request,'Payment Done! please checkout your order status')

            return redirect('/')
        else:
            messages.error(request,'Payment Failed')
            return redirect('cart')
    else:
        messages.error(request,'Invalid Session')
        return redirect('cart')
    
@login_required
def myOrders(request):
    user = request.user
    context ={
        'order': Order.objects.filter(user=user)
    }
    return render(request,'mainpage/my_order.html',context)