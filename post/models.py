from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to = 'profile_photos/', null=True)
    bio = models.CharField(max_length =300)
    contact = models.CharField(max_length =30)    

class Project(models.Model):
    title = models.CharField(max_length =30)
    project_image = models.ImageField(upload_to = 'landing_images/', null=True)
    description = models.CharField(max_length =300)
    # link = 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # date = models.DateTimeField(auto_now_add=True)
