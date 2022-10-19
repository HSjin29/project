from email.policy import default
from django.db import models


class USER(models.Model):
    idx=models.AutoField(primary_key=True)
    id=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    age=models.IntegerField(null=True, default=0)
    email=models.CharField(max_length=200, null=True)
    phone=models.IntegerField(null=True,default=0)
    job=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    add=models.CharField(max_length=255)
    

class Login(models.Model):
    log_id = models.CharField(max_length=10)
    log_password = models.CharField(max_length=50)




