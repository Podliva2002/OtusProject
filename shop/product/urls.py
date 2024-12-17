from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, ProductViewSet, BasketViewSet, BasketAllViewSet

app_name = 'shop_api'

router = DefaultRouter()

router.register(
    prefix=r'categories',
    viewset=CategoryViewSet,
    basename='category'
)

router.register(
    prefix=r'products',
    viewset=ProductViewSet,
    basename='product'
)

router.register(
    prefix=r'baskets',
    viewset=BasketAllViewSet,
    basename='basket'
)

urlpatterns = [
    path('basket/<int:user_id>', BasketViewSet.as_view({'get': 'list'}), name='basket'),
    *router.urls,
]
