from django.urls import path
from .viewsets import CategoryViewSet,SupplyViewSet,OrderDetailViewSet,OrderViewSet,UserViewSet,GroupViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'category',CategoryViewSet)
router.register(r'supply',SupplyViewSet,base_name='Supply')
router.register(r'order',OrderViewSet)
router.register(r'orderdetail',OrderDetailViewSet)
router.register(r'user',UserViewSet)
router.register(r'group',GroupViewSet)

urlpatterns =router.urls
