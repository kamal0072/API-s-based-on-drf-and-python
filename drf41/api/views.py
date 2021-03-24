from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SingerSerializer,SongSerializer
from .models import Singer,Song
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination


class MyPageNumberPagination(PageNumberPagination):
    page_size=2

class SingerViewSet(viewsets.ModelViewSet):
    queryset=Singer.objects.all()
    serializer_class=SingerSerializer
    filter_backends=[OrderingFilter]
    ordering_fields=['name']
    pagination_class=MyPageNumberPagination


class SongViewSet(viewsets.ModelViewSet):
    queryset=Song.objects.all()
    serializer_class=SongSerializer
    filter_backends=[OrderingFilter]
    ordering_fields=['singer']
    pagination_class=MyPageNumberPagination
