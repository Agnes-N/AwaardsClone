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
   
class CommentTestClass(TestCase):

    def setUp(self):
     
        self.user1 = User(username = 'aggy')
        self.user1.save()

        self.nature = Profile(2,user = self.user1,bio='kind')
        self.nature.save_profile()

        self.james = Project(2,title = 'James',description = 'beautiful',user=self.user1,project_image = "image")
        self.james.save_projects()
      
        self.comm = Comments(comment = 'leaves',commented_project = self.james,posted_by = self.nature)
        self.comm.save_comments()

 
    def test_instance(self):

        self.assertTrue(isinstance(self.comm,Comments))    
        
    def test_save_method(self):
        '''
        test image by save
        '''
        self.comm.save_comments()
        comm = Comments.objects.all()
        self.assertTrue(len(comm)>0) 

    def test_delete_method(self):
        '''
        test of delete image
        '''
  
        Comments.objects.all().delete()
   
class ProfileTestClass(TestCase):
    '''
    profile test method
    '''
    def setUp(self):
        self.user1 = User(username='aggy')
        self.user1.save()
        self.nature = Profile(2,user=self.user1,bio='cool')
        self.nature.save_profile()

    def test_instance(self):
            self.assertTrue(isinstance(self.nature,Profile))

    def test_save_method(self):
            '''
            test profile by save
            '''
            self.nature.save_profile()
            comm = Profile.objects.all()
            self.assertTrue(len(comm)>0) 
    
    def test_delete_method(self):
            '''
            test of delete profile
            '''
            Profile.objects.all().delete()  
              