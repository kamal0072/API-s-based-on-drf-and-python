from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student


class StudentViewSet(viewsets.ModelViewSet):
    # queryset=Student.objects.filter(passby='kamal')
    # queryset=Student.objects.filter(passby='sonam')
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def get_queryset(self):
        user=self.request.user
        return Student.objects.filter(passby=user)    