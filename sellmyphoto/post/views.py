from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .Serializer import PostSerializer
from rest_framework import generics
from .models import Post
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class PostFeed(generics.ListCreateAPIView):
    # def post(self,request):

    #     data = request.data
    #     serializer_obj = PostSerializer(data)
    #     if serializer_obj.is_valid():
    #         serializer_obj.save()
    #         return Response(serializer_obj.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
        