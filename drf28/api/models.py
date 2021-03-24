from django.db import models
# from django.contrib.auth import user_logged_in
from django.db.models.signals import post_save
from django.conf import settings
from rest_framework.authtoken.models import Token

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    address=models.CharField(max_length=90)

#This Is the Signal of Authtoken 
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)
post_save.connect(create_auth_token,sender=settings.AUTH_USER_MODEL)
