from django.shortcuts import render
from rango.models import Category, Page
from rest_framework import viewsets
from .serializers import CategorySerializer, PageSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
