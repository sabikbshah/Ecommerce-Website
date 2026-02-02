from .models import *




def setting(request):

    context = {
        'data': Setting.objects.last()
    }
    return context