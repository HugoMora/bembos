from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from .serializers import UserSerializer,GroupSerializer,CategorySerializer,SupplySerializer,OrderSerializer,OrderDetailSerializer
from .models import Category,Supply,Order,OrderDetail
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    #permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class=CategorySerializer
    queryset = Category.objects.all()
    #permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

class SupplyViewSet(viewsets.ModelViewSet):
    serializer_class=SupplySerializer
    #permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)
    # queryset = Componente.objects.all()

    def get_queryset(self):
        queryset = Supply.objects.all()
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(id_category=category)
        return queryset


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class=OrderSerializer
    queryset = Order.objects.all()
    #permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)
    #lookup_field='id_orden'

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return DetalleOrdenSerializer
    #     else:
    #         return DetalleOrdenSerializer

class OrderDetailViewSet(viewsets.ModelViewSet):
    serializer_class=OrderDetailSerializer
    queryset = OrderDetail.objects.all()
    #permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)