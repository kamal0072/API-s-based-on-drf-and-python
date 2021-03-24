from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.pagination import PageNumberPagination



class StudentApiView(GenericAPIView,ListModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    
    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)

class StudentCreate(GenericAPIView,CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)

class StudentRetrieve(GenericAPIView,RetrieveModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)

class StudentUpdate(GenericAPIView,UpdateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)

class StudentDestry(GenericAPIView,DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def delete(self,request,*args, **kwargs):
        return self.delete(request,*args, **kwargs)

