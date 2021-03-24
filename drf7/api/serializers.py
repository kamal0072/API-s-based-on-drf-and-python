from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    # name=serializers.CharField(read_only=True)
    # c_name=serializers.CharField(read_only=True)
    class Meta:
        model=Student
        fields=['c_name','c_address','c_moblile','c_dob']
      