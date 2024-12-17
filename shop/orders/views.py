from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]
    queryset = (
        Order.objects
        .select_related('buyer')
        .all()
    )


class UserOrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Order.objects.filter(buyer=user_id)

