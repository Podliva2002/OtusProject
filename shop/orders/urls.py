from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import OrderViewSet, UserOrderViewSet

app_name = 'order_api'

router = DefaultRouter()

router.register(
    prefix=r'orders',
    viewset=OrderViewSet,
    basename='order'
)


urlpatterns = [
    path('order/<int:user_id>', UserOrderViewSet.as_view({'get': 'list'}), name='basket'),
    *router.urls,
]
