from django.shortcuts import render
from .models import School
from .serializers import SchoolSerializer
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle,s
from .throttling import KamalThrottle

class SchoolModelViewSet(viewsets.ModelViewSet):
    queryset=School.objects.all()
    serializer_class=SchoolSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    # throttle_classes=[UserRateThrottle,AnonRateThrottle]
    # throttle_classes=[KamalThrottle,AnonRateThrottle]
    throttle_classes=[KamalThrottle,AnonRateThrottle]