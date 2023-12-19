from rest_framework import serializers

from nodes.models import NetworkNode, Contact, Product


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class NetworkNodeSerializer(serializers.ModelSerializer):
    contact_information = ContactSerializer(source='contact', read_only=True)
    product_list = ProductSerializer(source='product_set', many=True, read_only=True)

    class Meta:
        model = NetworkNode
        fields = ['id', 'name', 'node_type', 'contact', 'supplier', 'debt', 'product_list', 'contact_information',
                  'created_at']
        read_only_fields = ['debt', 'created_at']

