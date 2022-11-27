from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser
from rest_framework import filters


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [filters.OrderingFilter,]
    ordering_fields = ['date', ]
    permission_classes = [IsAuthenticatedOrReadOnly,]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

class ApplicationViewSet(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    filter_backends = [filters.OrderingFilter,]
    ordering_fields = ['date', 'category',]
    permission_classes = [IsAuthenticatedOrReadOnly,]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]