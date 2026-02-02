from django.urls import path
from .views import *





app_name = 'userpage' 

urlpatterns =[
     path('',homepage),
     path('all-products',userProducts,name='all-products'),
     path('product_details/<int:product_id>',productDetails,name ='product-details' ),
     path('addtocart/<int:product_id>',addToCart , name='addtocart'),
     path('cart',userCart,name='cart'),
     path('delete-cart/<int:cart_id>',deleteCart,name='delete-cart'),
     path('order-form/<int:cart_id>/<int:product_id>',orderForm,name='order-form'),
     path('stripe-checkout',stripeCheckout,name='stripe-checkout'),
     path('create_checkout_session/<int:order_id>/<int:cart_id>',create_checkout_session,name='create_checkout_session'),
     path('success/',stripeSuccess,name='stripe-success'),
     path('my-orders',myOrders,name='my-orders')
]