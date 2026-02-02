from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name

class Products(models.Model):
    SIZES = (
            ('S','S'),
            ('M','M'),
            ('L','L')
            )
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    original_price = models.DecimalField(max_digits=10,decimal_places=5)
    selling_price = models.DecimalField(max_digits=10,decimal_places=5)
    image = models.FileField(upload_to='static/uploads/')
    s_description = models.TextField(max_length=500)
    l_description = models.TextField(blank=True)
    size = models.CharField(max_length=30,choices=SIZES,null=True)
    trending = models.BooleanField(default = False)
    tags = models.CharField(max_length=50)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name
    
class Setting(models.Model):
    name = models.CharField(max_length=100)
    favicon = models.FileField(upload_to='static/uploads/')
    logo = models.FileField(upload_to='static/uploads/')
    email = models.EmailField()
    phone = models.CharField(max_length=14,validators = [MinLengthValidator(10),MaxLengthValidator(14)])
    address = models.CharField(max_length=1000)
    fb_link = models.URLField(blank = True)
    insta_link = models.URLField(blank = True)
    twitter_link = models.URLField(blank = True)

    def __str__(self):
        return self.name
    





