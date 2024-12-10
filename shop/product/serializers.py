from rest_framework import serializers, fields

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


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    category = CategoryHyperLinkSerializer(
        many=True,
        required=False,
    )


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ('id', 'product', 'quantity')
