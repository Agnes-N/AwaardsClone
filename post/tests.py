from django.test import TestCase
# Create your tests here.
from django.test import TestCase
from .models import Project,User,Profile,Comments
import datetime as dt

class ProjectsTestClass(TestCase):
    '''
    images test method
    '''
    def setUp(self):

        self.user1 = User(username='aggy')
        self.user1.save()
          
        self.image = Project(title = 'leaves',description = 'beautiful',user=self.user1,project_image = "image")
        self.image.save_projects()

 
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Project))

    def test_save_method(self):
        '''
        test image by save
        '''
        self.image.save_projects()
        images = Project.objects.all()
        self.assertTrue(len(images)>0) 
   

    def test_delete_method(self):
        '''
        test of delete image
        '''
       
        Project.objects.all().delete()
   

