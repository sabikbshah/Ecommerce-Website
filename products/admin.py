from django.contrib import admin
from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name','id','created_at']

    search_fields = ['name',]
    list_filter = ['created_at',]



admin.site.register(Category,CategoryAdmin)



class ProductsAdmin(admin.ModelAdmin):
        list_display = ['name','original_price','selling_price','vendor','created_at','image','trending','stock']
        search_fields = ['name','category','tag']
        list_filter = ['created_at','trending','vendor']

admin.site.register(Products,ProductsAdmin)


admin.site.register(Setting)
# admin.site.register(Trending)






