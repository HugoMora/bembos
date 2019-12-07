from rest_framework import viewsets
from .serializers import CategorySerializer,SupplySerializer,OrderSerializer,OrderDetailSerializer
from .models import Category,Supply,Order,OrderDetail

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class=CategorySerializer
    queryset = Category.objects.all()

class SupplyViewSet(viewsets.ModelViewSet):
    serializer_class=SupplySerializer
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
    #lookup_field='id_orden'

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return DetalleOrdenSerializer
    #     else:
    #         return DetalleOrdenSerializer

class OrderDetailViewSet(viewsets.ModelViewSet):
    serializer_class=OrderDetailSerializer
    queryset = OrderDetail.objects.all()