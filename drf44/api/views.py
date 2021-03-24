from django.shortcuts import render
from rest_framework import serializers
from .models import Student
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','name','roll','city']

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    filter_backends=[DjangoFilterBackend]