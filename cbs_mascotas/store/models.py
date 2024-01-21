from django.db import models
import datetime

#Categorías de Productos
class Category(models.Model):
    name =models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categorías'

#Usuario de Clientes
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        verbose_name_plural = 'Clientes'

#Todos los Productos
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField(max_length=300, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')    
    #Sale Stuff
    is_sale = models.BooleanField(default=False)
    sale_price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Productos'
    

#Compras del cliente
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=12, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product
    
    class Meta:
        verbose_name_plural = 'Compras'