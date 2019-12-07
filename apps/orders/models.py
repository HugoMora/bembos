from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    id                  = models.AutoField(primary_key=True)
    name         = models.CharField(max_length=200, blank=False, null=False)        
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name

class Supply(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=False, null=False)        
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image= models.ImageField(upload_to='pictures', max_length=255, null=True, blank=True)   
    price = models.DecimalField(max_digits=5,decimal_places=2)
    created_at = models.DateField('created at', auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Supply'
        verbose_name_plural = 'Supplies'
        ordering = ['name']

    def __str__(self):
        return self.name

class Order(models.Model):
    id = models.AutoField(primary_key=True)     
    description = models.CharField(max_length=200, blank=False, null=False)            
    customer = models.CharField(max_length=200, blank=False, null=False)        
    created_at = models.DateField('created at', auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['created_at']

    def __str__(self):
        return self.description

    @property
    def orderdetails(self):
        return self.orderdetail_set.all()

class OrderDetail(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    supply = models.ForeignKey(Supply,on_delete=models.CASCADE)
    band = models.IntegerField()
    quantity = models.IntegerField()
    
    class Meta:
        verbose_name = 'OrderDetail'
        verbose_name_plural = 'OrderDetails'
        ordering = ['id']

