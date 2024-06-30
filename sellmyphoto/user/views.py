from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .Serializer import AccountSerializr
from . import models
from rest_framework_simplejwt.views import TokenObtainPairView
from .Serializer import MyTokenObtainPairSerializer
from rest_framework import generics
from .models import Account
# Create your views here.


class RegisterUser(generics.CreateAPIView):
#     def post(self,request):
#         serializer = AccountSerializr(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# 
    queryset = Account.objects.all()
    serializer_class = AccountSerializr
# permission_classes = [IsAuthenticated]
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer