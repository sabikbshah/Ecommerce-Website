from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.




def aboutpage(request):
    return render(request,'mainpage/Aboutpage.html')

def addCategory(request):
    if request.method == 'POST':
        cateform = CategoryForm(request.POST)
        if cateform.is_valid():
            cateform.save()
            messages.success(request,'Category added Successfully!!')
            return redirect('vendor-products:all-category')
        else:
            messages.error(request,'Category Added failed!!')
            return render('request','vendor/add_category.html',{'form':cateform})
    context={
        'form':CategoryForm()
    }
    return render(request,'vendor/add_category.html',context)
#__________________________________________CATEGORY______________________________________________________
# def allCategory(request):
#     # request.user.vendor
#     user = request.user
    
#     context = {
#         'category': Category.objects.all()
#     }
#     return render(request,'vendor/all_category.html',context)
def allCategory(request):
    # request.user.vendor
    user = request.user
    vendor = Vendor.objects.get(user = user)
    # query set that translates to dbquery 1/2method better one
    # using __fields to lookup field vendor
    categories = Category.objects.filter(products__vendor=vendor).distinct()

    
    context = {
        # 'category': Category.objects.filter(products = products)
        'category': categories
    }
    return render(request,'vendor/all_category.html',context)
#______________________________________________________________________________________________________

def deleteCategory(request,category_id):
    category = Category.objects.get(id = category_id)
    category.delete()
    messages.success(request,'Category deleted Successfully!!')
    return redirect('vendor-products:all-category')

def updateCategory(request,category_id):
    category = Category.objects.get(id = category_id)
    if request.method == 'POST':
        cateform = CategoryForm(request.POST,instance=category)
        if cateform.is_valid():
            cateform.save()
            messages.success(request,'Category Updated Successfully!!')
            return redirect('all-category')
        else:
            messages.error(request,'Category update failed!!')
            return render('request','vendor/update_category.html',{'form':cateform})

    context ={
        'cateform': CategoryForm(instance = category)
    }

    return render(request,'vendor/update_category.html',context)
'''__________________________________________________________________________________________'''
# @login_required
# def addProducts(request):

#     if request.method == 'POST':
#         newproductform = ProductForm(request.POST,request.FILES) 
#         if newproductform.is_valid():
#             newproductform.save()
#             messages.success(request,'Product Added Successfully!!')
#             return redirect('/all-products')# works same as entering url first time which then calls view then get request.
#         else:
#             messages.error(request,'Product Add failed!!')
#             return render(request,'vendor/add_products.html',{'form':newproductform})

    
#     context = {
#         'form': ProductForm()
#     }
#     return render(request,'vendor/add_products.html',context)
@login_required
def addProducts(request):
    
    if request.method == 'POST':
        newproductform = ProductForm(request.POST,request.FILES) 
        if newproductform.is_valid():
            newproductform.save()
            messages.success(request,'Product Added Successfully!!')
            return redirect('vendor-products:all-products')# works same as entering url first time which then calls view then get request.
        else:
            messages.error(request,'Product Add failed!!')
            return render(request,'vendor/add_products.html',{'form':newproductform})

    
    context = {
        'form': ProductForm()
    }
    return render(request,'vendor/add_products.html',context)
'''__________________________________________________________________________________________'''

# def allProducts(request):
    
#     context ={
#         'products': Products.objects.all()
#     }
#     return render(request,'vendor/all_products.html',context)
@login_required
def allProducts(request):
    vendor = request.user.vendor # same as vendor = Vendor.objects.get(user=request.user) 
    context ={
        # 'products': Vendor.products.all() # when related_name= products is used method 2 djangostyle
        'products': Products.objects.filter(vendor = vendor) # this 'vendor' name is already as foreign key name
    }
    return render(request,'vendor/all_products.html',context)

def deleteProduct(request,product_id):
        product = Products.objects.get(id = product_id)
        product.delete()
        messages.success(request,'Product Deleted Successfully!!')
        return redirect('vendor-products:all-products')

def updateProduct(request,product_id):
    product = Products.objects.get(id = product_id)
    if request.method == 'POST':

        updateproductform = ProductForm(request.POST,instance = product)
        if updateproductform.is_valid():
            updateproductform.save()
            messages.success(request,'Product Updated!!')
            return redirect('vendor-products:all-products')
        else:
           messages.error(request,'Product Update failed!!')
           return render(request,'vendor/update_products.html',{'form':updateproductform})
    
    context = {
        'updateProductform' : ProductForm(instance = product)
    }
    return render(request,'vendor/update_products.html',context)

