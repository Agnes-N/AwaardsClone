from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length =30)
    project_image = models.ImageField(upload_to = 'landing_images/', null=True)
    description = models.CharField(max_length =300)
    link = models.URLField(max_length=128, db_index=True, unique=True, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    @classmethod
    def get_all_projects(cls):
        all_projects = cls.objects.all().prefetch_related('comments_set')
        return all_projects

    def save_projects(self):
        self.save()

    def delete_projects(self):
        self.delete()

    @classmethod
    def search_by_title(cls,search_term):
        certain_user = cls.objects.filter(title__icontains = search_term)
        return certain_user
        

    def __str__(self):
        return self.user

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to = 'profile_photos/', null=True)
    bio = models.CharField(max_length =300)
    contact = models.CharField(max_length =30)  
    projects = models.ForeignKey(Project,on_delete=models.CASCADE, null=True)

    @classmethod
    def get_profile(cls):
        all_profiles = cls.objects.all()
        return all_profiles

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete() 

class Comments(models.Model):
    comment = models.CharField(max_length = 250)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    posted_by = models.ForeignKey(Profile, on_delete=models.CASCADE, null = True)
    commented_project = models.ForeignKey(Project, on_delete=models.CASCADE, null = True)

    def save_comments(self):
        self.save()

    def delete_comments(self):
        self.delete()

    def __str__(self):
        return self.posted_by


class Rating(models.Model):
    design = models.PositiveIntegerField(default = 0,validators = [MaxValueValidator(10)])
    usability = models.PositiveIntegerField(default = 0,validators = [MaxValueValidator(10)])
    content = models.PositiveIntegerField(default = 0,validators = [MaxValueValidator(10)])
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    project = models.IntegerField(default = 0)