from django.shortcuts import render

# Create your views here.

def myStore(request):
    context = {
        'vendors' : 'None'
    }

    # return render(request,'vendor/dashboard.html',context)
    return render(request,'vendor/dashboard.html',context)