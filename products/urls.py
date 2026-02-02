from django.urls import path
from .views import *


app_name = 'vendor-products'


urlpatterns= [
   
    path('about',aboutpage),
    path('add-category',addCategory,name="add-category"),
    path('all-category',allCategory,name="all-category"),
    path("delete-category/<int:category_id>",deleteCategory,name="delete-category"),
    path("update-category/<int:category_id>",updateCategory,name="update-category"),
    
    path('add-products',addProducts,name="add-products"),
    path('all-products',allProducts,name = "all-products"),
    path('delete-product/<int:product_id>',deleteProduct,name="delete-product"),
    path('update-product/<int:product_id>',updateProduct,name="update-product")
]