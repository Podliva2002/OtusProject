from rest_framework import serializers

from .models import Category, Product, Basket


class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.SerializerMethodField()
    parent_name = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def get_subcategories(self, obj):
        subcategories = obj.subcategories.all()
        return CategorySerializer(subcategories, many=True).data

    def get_parent_name(self, obj):
        return obj.parentId.name if obj.parentId else None


class CategoryHyperLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'parentId', 'level',)


class ProductHyperLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name',)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    category = CategoryHyperLinkSerializer(
        many=True,
        required=False,
    )


class BasketSerializer(serializers.ModelSerializer):
    total_sum = serializers.SerializerMethodField()
    cost = serializers.SerializerMethodField()
    product_name = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ('id', 'user', 'image', 'product', 'product_name', 'quantity', 'cost', 'total_sum')

    def get_total_sum(self, obj):
        product = obj.product
        price = product.price
        return price * obj.quantity

    def get_cost(self, obj):
        product = obj.product
        price = product.price
        return price

    def get_product_name(self, obj):
        product = obj.product
        return product.name

    def get_image(self, obj):
        product = obj.product
        return f'http://localhost:8000{product.image.url}' if product.image else None
