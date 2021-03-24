from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser,DjangoModelPermissions,DjangoObjectPermissions,DjangoModelPermissionsOrAnonReadOnly
from rest_framework import viewsets
from .custompermissions import MyPermission

class StudentreadonlyModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[MyPermission]
    # # permission_classes=[IsAuthenticated]
    # # permission_classes=[IsAuthenticatedOrReadOnly]
    # # permission_classes=[IsAdminUser]
    # # permission_classes=[DjangoModelPermissionsOrAnonReadOnly]
    # permission_classes=[DjangoObjectPermissions]
    

