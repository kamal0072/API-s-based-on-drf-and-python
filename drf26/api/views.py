from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerailizer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerailizer
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]