from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from product.models import Category
from product.serializers import CategorySerializer
from rest_framework import authentication
from product.permissions import AdminOrReadonly

# Create your views here.

class CategoryCreateListView(ListCreateAPIView):
    permission_classes=[AdminOrReadonly]
    authentication_classes=[authentication.TokenAuthentication]

    serializer_class=CategorySerializer
    queryset=Category.objects.all()

class CategoryUpdateDeleteRetrive(RetrieveUpdateDestroyAPIView):

    permission_classes=[AdminOrReadonly]
    authentication_classes=[authentication.TokenAuthentication]

    serializer_class=CategorySerializer
    queryset=Category.objects.all()
    




