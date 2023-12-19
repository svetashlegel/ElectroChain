from rest_framework import viewsets, permissions, generics

from nodes.models import NetworkNode, Contact, Product
from nodes.serializers import NetworkNodeSerializer, ContactSerializer, ProductSerializer


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]


class NetworkNodeViewSet(viewsets.ModelViewSet):
    serializer_class = NetworkNodeSerializer
    queryset = NetworkNode.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
