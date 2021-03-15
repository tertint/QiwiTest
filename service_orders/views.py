from rest_framework.viewsets import ModelViewSet
from service_orders.models import Order
from service_orders.serializers import OrderSerializer


class OrderView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
