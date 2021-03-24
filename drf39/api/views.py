from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import LimitOffsetPagination

class MyLimitOffpagination(LimitOffsetPagination):
    limit_query_description=8
    default_limit=2
    limit_query_param='mylimit'
    max_limit=5



class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    filter_backends=[OrderingFilter]
    ordering_fields=['name']
    pagination_class=MyLimitOffpagination
    
