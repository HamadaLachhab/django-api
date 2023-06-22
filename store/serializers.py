from rest_framework import serializers
from decimal import Decimal
from .models import Product, Collection,Review

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    products_count = serializers.IntegerField(read_only=True)


  
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'slug', 'inventory', 'unit_price', 'price_with_tax', 'collection']

    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax')

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
  # id = serializers.IntegerField()
  # title = serializers.CharField(max_length=255)
  # price  = serializers.DecimalField(max_digits=5,decimal_places=2,source='unit_price')
  # price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
  # #collection   = CollectionSerializer()
  # collection = serializers.HyperlinkedRelatedField(
  #   queryset=Collection.objects.all(),
  #   view_name='collection-detail'
  # )
  # def calculate_tax(self,product:Product):
  #   return product.unit_price*Decimal(1.1)
  
  # def validate (self,data):
  #   if data['passowrd'] != data['confirm_password']:
  #     return serializers.ValidationError('Password do not match ')
  #   return data
  ## DESERIALIZE
  # def create(self,validated_data):
  #   product = Product(**validated_data)
  #   #product.other = 1
  #   product.save()
  #   return product
  # def update(self, instance, validated_data):
  #   instance.unit_price=validated_data.get('unit_price')
  #   instance.save()
  #   return instance
  
  
  
  
  
    
# class CollectionSerializer ( serializers.Serializer):
#   id = serializers.IntegerField()
#   title = serializers.CharField(max_length=255)
  
# class ProductSerializer ( serializers.Serializer):
#   id = serializers.IntegerField()
#   title = serializers.CharField(max_length=255)
#   price  = serializers.DecimalField(max_digits=5,decimal_places=2,source='unit_price')
#   price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
#   #collection   = CollectionSerializer()
#   collection = serializers.HyperlinkedRelatedField(
#     queryset=Collection.objects.all(),
#     view_name='collection-detail'
#   )
#   def calculate_tax(self,product:Product):
#     return product.unit_price*Decimal(1.1)
    
    
    
class ReviewSerializer (serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','date','name','description']
    def create(self,validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id,**validated_data)