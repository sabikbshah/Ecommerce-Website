from django.contrib import admin
from .models import Vendor

# Register your models here.


class VendorAdmin(admin.ModelAdmin):
        list_filter = ['approved']

admin.site.register(Vendor,VendorAdmin)