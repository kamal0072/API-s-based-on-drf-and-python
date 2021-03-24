from django.shortcuts import render
from .models import School
from .serializers import SchoolSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination

class Mypagination(PageNumberPagination):
    page_size=2
    

class SchoolModelViewSet(viewsets.ModelViewSet):
    queryset=School.objects.all()
    serializer_class=SchoolSerializer
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    pagination_class=Mypagination
    