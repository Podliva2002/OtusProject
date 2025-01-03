from django.contrib.auth.models import User
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, pagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Category, Product, Basket
from .serializers import CategorySerializer, ProductSerializer, BasketSerializer


# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    queryset = (
        Category.objects
        .select_related('parentId')
        .all()
    )


class ProductPagination(pagination.PageNumberPagination):
    page_size = 4

    def get_paginated_response(self, data):
        total_pages = self.page.paginator.num_pages  # Общее количество страниц
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,  # Общее количество элементов
            'total_pages': total_pages,  # Общее количество страниц
            'results': data
        })


class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['category']


class ProductViewSet(viewsets.ModelViewSet):
    queryset = (
        Product.objects
        .prefetch_related('category')
        .all()
    )
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated()]  # Требует авторизации для создания и изменения
        return [AllowAny()]

    def get_queryset(self):
        return Product.objects.filter(inStock=True)


class BasketViewSet(viewsets.ModelViewSet):
    serializer_class = BasketSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Basket.objects.filter(user=user_id)


class BasketAllViewSet(viewsets.ModelViewSet):
    serializer_class = BasketSerializer
    queryset = (
        Basket.objects
        .select_related('user', 'product')
        .all()
    )
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        print(request.data)
        user = request.data['user']
        product_id = request.data['product']
        quantity = int(request.data.get('quantity', 1))

        product = Product.objects.get(id=product_id)
        user = User.objects.get(id=user)

        basket, created = Basket.objects.get_or_create(user=user, product=product)

        if not created:
            basket.quantity += quantity
            basket.save(update_fields=['quantity'])

        return Response(BasketSerializer(basket).data)
