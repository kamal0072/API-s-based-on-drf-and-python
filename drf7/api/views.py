from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.viewsets import views
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

class StudentViewSet(GenericAPIView,ListModelMixin):
    queryset=Student
    serializer_class=StudentSerializer
    
    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    