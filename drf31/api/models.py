from django.db import models

# Create your models here.
class School(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=90)
    roll=models.IntegerField()
    email=models.EmailField(max_length=80)
    # admission=models.DateField()
    addmission_confirm=models.DateTimeField()