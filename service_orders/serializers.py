from rest_framework.serializers import ModelSerializer
from service_orders.models import Order


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
