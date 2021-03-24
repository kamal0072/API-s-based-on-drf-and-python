from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    filter_backends=[SearchFilter]
    # filterset_fields=['name']
    # search_fields=['name']
    # search_fields=['^name']
    # search_fields=['^city']
    # search_fields=['=city']
    search_fields=['city']