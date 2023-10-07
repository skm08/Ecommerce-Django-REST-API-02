from rest_framework import generics
from rest_framework import permissions

from .models import Category, Product
from .serializers import (
    ProductSerializer, 
    CategorySerializer, 
    RetrieveProductSerializer,
    RetrieveCategorySerializer,
    )


class ListProduct(generics.ListAPIView):
    permission_classes=[permissions.AllowAny, ]
    serializer_class=ProductSerializer

    def get_queryset(self):
        return Product.objects.order_by('-id')
    
class ListCategory(generics.ListAPIView):
    permission_classes=[permissions.AllowAny, ]
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class RetrieveProduct(generics.RetrieveAPIView):
    permission_classes=[permissions.AllowAny, ]
    queryset=Product.objects.all()
    serializer_class=RetrieveProductSerializer
    lookup_field="slug"

class RetrieveCategory(generics.RetrieveAPIView):
    permission_classes=[permissions.AllowAny, ]
    queryset=Category.objects.all()
    serializer_class=RetrieveCategorySerializer
    lookup_field="slug"

class CreateProduct(generics.CreateAPIView):
    permission_classes=[permissions.IsAdminUser, ]
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class UpdateProduct(generics.UpdateAPIView):
    permission_classes=[permissions.IsAdminUser, ]
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class DestroyProduct(generics.DestroyAPIView):
    permission_classes = [permissions.IsAdminUser, ]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer