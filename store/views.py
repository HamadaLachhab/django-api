from django.db.models.aggregates import Count
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .models import Collection, Product,OrderItem, Review
from .serializers import CollectionSerializer, ProductSerializer , ReviewSerializer





class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    queryset = Product.objects.all()
    filterset_fields = ['collection_id']
    # def get_queryset(self):
    #     queryset= Product.objects.all()
    #     collection_id = self.request.query_params.get('collection_id')
    #     if collection_id is not None:
    #         queryset = queryset.filter(collection_id=collection_id)
    #     return queryset
    def get_serializer_context(self):
        return {'request': self.request}
    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(prodcut_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Product cannot be deleted because it is associated with an order item.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)    
        return super().destroy(request, *args, **kwargs)
       
    
    #GENERIC  CREATE 
# class ProductList(ListCreateAPIView):
#     queryset= Product.objects.select_related('collection').all()
#     serializer_class = ProductSerializer
#     # def get_queryset(self):
#     #     return Product.objects.select_related('collection').all()
    
#     # def get_serializer_class(self):
#     #     return ProductSerializer
    
#     def get_serializer_context(self):
#         return {'request': self.request}
   
       
# class ProductList(APIView):
    
#     def get(self,request):  
#         queryset = Product.objects.select_related('collection').all()
#         serializer = ProductSerializer(
#             queryset, many=True, context={'request': request})
#         return Response(serializer.data)
    
#     def post(self,request): 
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
      
    
# @api_view(['GET', 'POST'])
# def product_list(request):
#     if request.method == 'GET':
#         queryset = Product.objects.select_related('collection').all()
#         serializer = ProductSerializer(
#             queryset, many=True, context={'request': request})
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#         #class generic view 
# class ProductDetail(RetrieveUpdateDestroyAPIView):
#     queryset=Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field='id'
#     def delete(self,request,id):
#         product = get_object_or_404(Product, pk=id)
#         if  product.orderitems.count() > 0:
#             return Response({'error': 'Product cannot be deleted because it is associated with an order item.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
    
      
        #class based 

# class ProductDetail(APIView):
    
#     def get(self,request,id):
#         product = get_object_or_404(Product, pk=id)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
    
#     def put(self,request,id):
#         product = get_object_or_404(Product, pk=id)
#         serializer = ProductSerializer(product, data=request.data,partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     def delete(self,request,id):
#         product = get_object_or_404(Product, pk=id)
#         if  product.orderitems.count() > 0:
#             return Response({'error': 'Product cannot be deleted because it is associated with an order item.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        
   #function based     
        
# @api_view(['GET', 'PUT', 'DELETE'])
# def product_detail(request, id):
#     product = get_object_or_404(Product, pk=id)
#     if request.method == 'GET':
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = ProductSerializer(product, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         if product.orderitems.count() > 0:
#             return Response({'error': 'Product cannot be deleted because it is associated with an order item.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



class CollectionViewSet(ModelViewSet):
    queryset= Collection.objects.annotate(products_count=Count('products')).all()
    serializer_class=CollectionSerializer
    
    def destroy(self,request,pk):
        collection = get_object_or_404(Collection,pk=pk)
        if collection.products.count() > 0:
            return Response({'error': 'Collection cannot be deleted because it includes one or more products.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    




 
    
# @api_view(['GET', 'POST']) 
# def collection_list(request):
#     if request.method == 'GET':
#         queryset = Collection.objects.annotate(products_count=Count('products')).all()
#         serializer = CollectionSerializer(queryset, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CollectionSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'PUT', 'DELETE'])
# def collection_detail(request, pk):
#     collection = get_object_or_404(
#         Collection.objects.annotate(
#             products_count=Count('products')), pk=pk)
#     if request.method == 'GET':
#         serializer = CollectionSerializer(collection)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = CollectionSerializer(collection, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         if collection.products.count() > 0:
#             return Response({'error': 'Collection cannot be deleted because it includes one or more products.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         collection.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



class ReviewViewSet(ModelViewSet):
    queryset= Review.objects.all()
    serializer_class = ReviewSerializer
    def get_serializer_context(self):
        return {'product_id':self.kwargs['product_pk']}