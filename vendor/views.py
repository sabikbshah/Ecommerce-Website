from django.shortcuts import render

from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def myStore(request):
    context = {
        'vendors' : 'None'
    }

    # return render(request,'vendor/dashboard.html',context)
    return render(request,'vendor/dashboard.html',context)