from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
# Create your views here.




def aboutpage(request):
    return render(request,'mainpage/Aboutpage.html')

def addCategory(request):
    if request.method == 'POST':
        cateform = CategoryForm(request.POST)
        if cateform.is_valid():
            cateform.save()
            messages.success(request,'Category added Successfully!!')
            return redirect('all-category')
        else:
            messages.error(request,'Category Added failed!!')
            return render('request','vendor/add_category.html',{'form':cateform})
    context={
        'form':CategoryForm()
    }
    return render(request,'vendor/add_category.html',context)

def allCategory(request):
    context = {
        'category': Category.objects.all()
    }
    return render(request,'vendor/all_category.html',context)

def deleteCategory(request,category_id):
    category = Category.objects.get(id = category_id)
    category.delete()
    messages.success(request,'Category deleted Successfully!!')
    return redirect('all-category')

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

def addProducts(request):

    if request.method == 'POST':
        newproductform = ProductForm(request.POST,request.FILES) 
        if newproductform.is_valid():
            newproductform.save()
            messages.success(request,'Product Added Successfully!!')
            return redirect('/all-products')# works same as entering url first time which then calls view then get request.
        else:
            messages.error(request,'Product Add failed!!')
            return render(request,'vendor/add_products.html',{'form':newproductform})

    
    context = {
        'form': ProductForm()
    }
    return render(request,'vendor/add_products.html',context)

def allProducts(request):
    context ={
        'products': Products.objects.all()
    }
    return render(request,'vendor/all_products.html',context)

def deleteProduct(request,product_id):
        product = Products.objects.get(id = product_id)
        product.delete()
        messages.success(request,'Product Deleted Successfully!!')
        return redirect('all-products')

def updateProduct(request,product_id):
    product = Products.objects.get(id = product_id)
    if request.method == 'POST':

        updateproductform = ProductForm(request.POST,instance = product)
        if updateproductform.is_valid():
            updateproductform.save()
            messages.success(request,'Product Added Successfully!!')
            return redirect('all-products')
        else:
           messages.error(request,'Product Update failed!!')
           return render(request,'vendor/update_products.html',{'form':updateproductform})
    
    context = {
        'updateProductform' : ProductForm(instance = product)
    }
    return render(request,'vendor/update_products.html',context)

