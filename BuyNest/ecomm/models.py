from django.db import models

class UserData(models.Model):
    
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    email= models.EmailField()
    password= models.CharField(max_length=100)
