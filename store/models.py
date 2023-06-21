from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


# MANY To many  PROMOTION - PRODUCT

class Promotion (models.Model):
  description = models.CharField(max_length=255)
  discount = models.FloatField()
  #product_set  return all product that product refer to 



  
class Product(models.Model):
  title=models.CharField(max_length=255) #(primary=True)
  description = models.TextField(default="",blank=True)
  slug = models.SlugField(null=True)
  # digit after decimal and before
  unit_price = models.DecimalField(max_digits=6,decimal_places=2,  validators=[MinValueValidator(1)])
  inventory= models.IntegerField()
  last_update=models.DateTimeField(auto_now=True) # auto_add_now in creation
  collection = models.ForeignKey('Collection',on_delete=models.PROTECT,related_name='products')
  promotions = models.ManyToManyField(Promotion,related_name='products_set')
  
  def __str__(self) -> str:
    return self.title
  
  class Meta:
    ordering=['title']
  
class Collection(models.Model):  
  title = models.CharField(max_length=255)
  featured_product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True,related_name='+',blank=True) # this tell  django to not create reverse relation
  def __str__(self) -> str:
    return self.title
  class Meta:
    ordering=['title']
  
  
class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['first_name', 'last_name']

 
class Order (models.Model):
  placed_at = models.DateTimeField(auto_now_add=True)
  STAT_PEND ='P'
  STAT_FAIL = 'F'
  STAT_COMP ='C'
  PAYMENT_STATUS_CHOICES = [(STAT_COMP,'complete'),(STAT_FAIL,'Failed'),
                            (STAT_PEND,'pending')]
  payment_status = models.CharField(max_length=1,choices=PAYMENT_STATUS_CHOICES,default=STAT_PEND )
  customer = models.ForeignKey(Customer,on_delete=models.PROTECT  )
  


class OrderItem(models.Model):
  order = models.ForeignKey(Order,on_delete=models.PROTECT)#add related_name argument to change the conventional name orderitem_set
  product = models.ForeignKey(Product,on_delete=models.PROTECT,related_name="orderitems")
  quantity = models.PositiveSmallIntegerField()
  unit_price = models.DecimalField(max_digits=6, decimal_places=2) 
  
  
  
#one to one 
# class Adress(models.Model):
#    street = models.CharField(max_length=255)
#    city = models.Char  Field(max_length=255)
#    customer = models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True) # if it is nullable we use SET_NULL
   
#One to Many
class Adress(models.Model):
   street = models.CharField(max_length=255)
   city = models.CharField(max_length=255)
   customer = models.ForeignKey(Customer,on_delete=models.CASCADE) # if it is nullable we use SET_NULL


class Cart (models.Model):
  created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
  cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
  product = models.ForeignKey(Product,on_delete=models.CASCADE)
  quantity = models.PositiveSmallIntegerField()