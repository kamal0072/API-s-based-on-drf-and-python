from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination

class Mypagination(PageNumberPagination):
    page_size=2
    page_query_param='mypage'
    page_size_query_param='records'
    page_size_query_description='pagination'
    page_query_description='kk'
    max_page_size=10
    # last_page_strings = 2

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    filter_backends=[OrderingFilter]
    ordering_fields=['name']
    pagination_class=Mypagination
    
