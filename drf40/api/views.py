from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import CursorPagination


class Mycursorpagination(CursorPagination):
    page_size=5
    ordering='name'
    



class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    # filter_backends=[OrderingFilter]
    # ordering_fields=['name']
    pagination_class=Mycursorpagination

    
