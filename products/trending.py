from .models import *




def setting(request):
    

    context = {
        'trending_data' : Products.objects.filter(trending = True)
    }
    return context
