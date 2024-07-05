from decimal import Decimal
from rest_framework import serializers
from store.models import Product, Collection


# we just select some fields from the defined models


# class CollectionSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)


# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
    
#     # unit_price = serializers.DecimalField(max_digits=6, decimal_places=2)
#     price = serializers.DecimalField(max_digits=6, decimal_places=2, source="unit_price")
    
#     # price_with_tax = serializers.SerializerMethodField(
#     #     method_name="calculate_tax"
#     # )
#     price_with_tax = serializers.SerializerMethodField(
#         method_name="calculate_tax"
#     )

#     # serialize a relationship
#     # collection = serializers.PrimaryKeyRelatedField(
#     #     queryset=Collection.objects.all()
#     # )
#     # collection = serializers.StringRelatedField()
#     # collection = CollectionSerializer()

#     # serializing the relationship as a json object
#     collection = serializers.HyperlinkedRelatedField(
#         queryset=Collection.objects.all(),
#         view_name="collection-detail"
#     )

#     def calculate_tax(self, product: Product):
#         return product.unit_price * Decimal(1.1)


# directly serializing the product model
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = [
            'id', 'title'
        ]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'title', "slug", "inventory", "description", 
            'unit_price', 'collection', 'price_with_tax'
        ]

    # collection = serializers.HyperlinkedRelatedField(
    #     queryset=Collection.objects.all(),
    #     view_name="collection-detail"
    # )
    price_with_tax = serializers.SerializerMethodField(
        method_name="calculate_tax"
    )

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
    
    # def validate(self, data):
    #     if data['password'] != data['confirm_password']:
    #         return serializers.ValidationError('Passwords do not match')
    #     else:
    #         return data

    # to overwrite how a object is created
    # def create(self, validated_data):
    #     product = Product(**validated_data)
    #     product.other = 1
    #     product.save()
    #     return product
    
    # # overwrite how a product is updated
    # def update(self, instance, validated_data):
    #     instance.unit_price = validated_data.get('unit_price')
    #     instance.save()
    #     return instance