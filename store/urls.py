from django.urls import path 
from rest_framework.routers import SimpleRouter , DefaultRouter
from rest_framework_nested import routers
from . import views 
from pprint import pprint

#nested route 
router = routers.DefaultRouter()
router.register('products',views.ProductViewSet,basename='products')
router.register('collections',views.CollectionViewSet)

products_router=routers.NestedDefaultRouter(router,'products',lookup='product')
products_router.register('reviews',views.ReviewViewSet,basename='product-reviews')



# view set route
# router = SimpleRouter()
# router.register('products',views.ProductViewSet)
# router.register('collections',views.CollectionViewSet)
# pprint(router.urls)
# URLConf
urlpatterns=router.urls + products_router.urls
# urlpatterns = [
#     path('products/', views.ProductList.as_view()),
#     path('products/<int:pk>/', views.ProductDetail.as_view()),
#     path('collections/', views.CollectionList.as_view()),
#     path('collections/<int:pk>/', views.collection_detail, name='collection-detail'),
# ]
