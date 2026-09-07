from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from api.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import permissions,authentication
from rest_framework.response import Response
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
