from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,RetrieveUpdateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from api.serializers import UserSerializer,AddressSerializer,UserProfileserializer
from rest_framework.views import APIView
from rest_framework import permissions,authentication
from rest_framework.response import Response
from api.models import User,Address,Profile
from api.permissions import OwnerOnly
# Create your views here.
class RegisterView(CreateAPIView):
    serializer_class=UserSerializer

class LogoutView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def post(self,request):
        request.auth.delete()
        return Response({"msg":"Logged out"})
    
class InfoView(APIView):
    
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]


    def get(self,request):
        user=request.user
        return Response({"username":user.username,"phone":user.phone,"email":user.email})




class ProfileRetrieveUpdateView(RetrieveUpdateAPIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[OwnerOnly]

    serializer_class=UserProfileserializer

    def get_object(self):
        return Profile.objects.get(user=self.request.user)


class AddressCreateList(ListCreateAPIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[OwnerOnly]

    serializer_class=AddressSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)
    
class AddressUpdateDelete(RetrieveUpdateDestroyAPIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[OwnerOnly]

    serializer_class=AddressSerializer

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)