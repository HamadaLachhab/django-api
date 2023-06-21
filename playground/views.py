from django.shortcuts import render
from django.http  import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q , F , Value,Func,ExpressionWrapper , DecimalField
from django.db.models.aggregates import  Count ,Max, Min, Avg
from django.db.models.functions import Concat
from django.db import transaction ,connection
from store.models import Product,Collection ,OrderItem, Order,Customer
from tags.models import TaggedItem
# Create your views here.
#request -> response   
# Action 
 
def say_hello(request):
 # return HttpResponse('HELLO LL')
 #query_set = Product.objects.filter(unit_price__range=(20,30))
 #query_set = Product.objects.filter(collection__id__range=(1,2,3))
 #query_set = Product.objects.filter(title__icontains='coffee') startwith
 #query_set = Product.objects.filter(last_update__year=2021)
 #query_set = Product.objects.filter(description__isnull=True)
 #query_set = Product.objects.filter(inventory__lt=10,unit_price__lt=20) or chained filter
 # Or #query_set = Product.objects.filter(Q(inventory_lt=10)| Q(unit_price__lt=20 ))
 #query_set = Product.objects.filter(inventory=F('unit_price'))
 #sorting
 #query_set=Product.objects.order_by('unit_price','-title').reverse() # up ascending and title descending and then reverse
 #product = Product.objects.order_by('unit_price')[0]
 #limiting 
 #query_set = Product.objects.all()[5:10]
 #query_set = Product.objects.values('id','title','collection__title')
 #query_set = Product.objects.filter(pk=F(order_item))
 #exercice
 #query=OrderItem.objects.values('product_id').distinct()
 #query_set=Product.objects.filter(id__in=query)
 #defering 
 #query_set = Product.objects.only('id','title')
 #query_set = Product.objects.defer('title') //ignore 
 #query_set =
 #selecting related objects (1)
 #query_set = Product.objects.select_related("collection__someotherfield").all()
 #prefetch_related (n)  get all promotion to a product  
 #query_set = Product.objects.prefetch_related("promotion").all() 
 #query_set = Order.objects.select_related("customer").prefetch_related("orderitem_set__product"
 #                                                           ).order_by("placed_at")[:5]
 # Aggregate function 
 #result =Product.objects.filter(collection__id).aggregate(count=Count('id'),min_price=Min('unit_price'))
 #Annotating  adding field  
 #query_set=Customer.objects.annotate(is_new=Value(True))
 #query_set=Customer.objects.annotate(is_new=F('id'))
 #calling database func
 #query_set = Customer.objects.annotate(
   #CONCAT
 #  full_name=Func(F('first_name'),Value(' '),F('last_name'),function='CONCAT')
 #)
 #query_set = Customer.objects.annotate(full_name=Concat('first_name',Value(' '),'last_name'))
 #query_set = Customer.objects.annotate( number_order=Count('order'))
 #Expression wrappers 
  #  disc =ExpressionWrapper(F('unit_price')*0.8, output_field=DecimalField())
  #  query_set = Product.objects.annotate(discou=disc)
  #querying GEneric relationship
  
  #  contenttype= ContentType.objects.get_for_model(Product)# we get  content type  object 
  #  query_set=TaggedItem.objects \
  #    .select_related('tag')  \
  #    .filter(
  #    content_type=contenttype,
  #    object_id=1
  #  )
 #query_set=TaggedItem.objects.get_tags_for(Product,1)
 #QuerySET CACHE ( order matter )
 #CREATING ObJECT
#  collection = Collection
#  collection.title = 'video games'
#  collection.featured_product=Product(pk=1)
 #collection.featured_product_id = 1 #other way
#  collection.save()
 #UPDATING ObJECT
#  collection = Collection.objects.get(pk=11)
#  collection.featured_product=Product(pk=1)
 #collection.featured_product_id = 1 #other way
#  collection.save()
 #Collection.objects.filter().update(featured_product=xx)
 #DELETTING 
#  collection.objects.filter(id_get=5).delete()
 #TRANSACTION
#  with transaction.atomic():
#   order = Order()
#   order.customer_id=1
#   order.save()
  
#   item = OrderItem()
#   item.order=order
#   item.product_id=1 # for example if we place here -1 there is error but  it will not create order  
#   item.quantity = 1 
#   item.unit_price = 10 
#   item.save()
#  query__set=Product.objects.raw('SELECT * FROM store_product')
#  cursor = connection.cursor()
#  cursor.execute('')
#  cursor.close()
#  with connection.cursor() as cursor:
#    cursor.execute()    # the cursor will be closed automa
 
 return render(request,'hello.html',{'result':'result' ,'tags':list(query__set)})
    