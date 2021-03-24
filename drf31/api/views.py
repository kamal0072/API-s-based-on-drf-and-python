from django.shortcuts import render
from .models import School
from .serializers import SchoolSerializer
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

class SchoolModelViewSet(viewsets.ModelViewSet):
    queryset=School.objects.all()
    serializer_class=SchoolSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]