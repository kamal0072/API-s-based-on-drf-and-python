from django.db import models

class Student(models.Model):
    c_name=models.CharField(max_length=120)
    c_address=models.CharField(max_length=130)
    c_moblile=models.IntegerField()
    c_dob=models.DateField()