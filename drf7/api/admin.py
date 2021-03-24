from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','c_name','c_address','c_moblile','c_dob']
    
