from django.shortcuts import render
from .models import School
from .serializers import SchoolSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.throttling import ScopedRateThrottle


class StudentListApi(ListAPIView):
    queryset=School.objects.all()
    serializer_class=SchoolSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='viewstu'
    

class StudentCreateApi(CreateAPIView):
     queryset=School.objects.all()
     serializer_class=SchoolSerializer
     throttle_classes=[ScopedRateThrottle]
     throttle_scope='viewstu'



    
class StudentRetreiveApi(CreateAPIView):
     queryset=School.objects.all()
     serializer_class=SchoolSerializer
     throttle_classes=[ScopedRateThrottle]
     throttle_scope='viewstu'


    
class StudentUpdateApi(CreateAPIView):
     queryset=School.objects.all()
     serializer_class=SchoolSerializer
     throttle_classes=[ScopedRateThrottle]
     throttle_scope='modufistu'



class StudentRetreiveUpdateDestroyApi(CreateAPIView):
     queryset=School.objects.all()
     serializer_class=SchoolSerializer
     throttle_classes=[ScopedRateThrottle]
     throttle_scope='modufistu'

