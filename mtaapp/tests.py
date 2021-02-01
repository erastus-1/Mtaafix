from .models import *
from django.test import TestCase
from django.contrib.auth.models import User


# Create your tests here.
class NeighborhoodTestClass(TestCase):
    def setUp(self):
        self.new_user = User(username='erass',email='test@gmail.com')
        self.new_user.save()
        self.utawala = Neighbourhood(name='mutwech',location='utawala',image='image.jpg',occupants=5)
        self.utawala.save()

    def tearDown(self):
        User.objects.all().delete()
        Neighbourhood.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.utawala,Neighbourhood))

    def test_save_neighborhood(self):
        self.utawala.save_neighborhood()
        neighborhood = Neighbourhood.objects.all()
        self.assertTrue(len(neighborhood)>0)



class BusinessTestClass(TestCase):
    def setUp(self):
        self.new_user=User(username="erass",email="test@gmail.com")
        self.new_user.save()
        self.utawala = Neighbourhood(name='mutwech',location='utawala',occupants_count=5,admin=self.new_user)
        self.utawala.save_neighborhood()
        self.palour = Business(name='palour',email='test@gmail.com',user=self.new_user,neighborhood=self.utwala)
        self.palour.save()

    def tearDown(self):
        User.objects.all().delete()
        Neighbourhood.objects.all().delete()
        Business.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.palour,Business))

    def test_save_business(self):
        self.palour.save_business()
        business =  Business.objects.all()
        self.assertTrue(len(business)>0)



class PostTestClass(TestCase):
    def setUp(self):
        self.new_user=User(username="erass",email="test@gmail.com")
        self.new_user.save()
        self.utawala = Neighbourhood(name='mutwech',location='utawala',occupants_count=5,admin=self.new_user)
        self.utawala.save_neighborhood()
        self.erass = User(name="mutwech",user=self.new_user,neighborhood=self.utawala)
        self.erass.save_user()
        self.new_post=Post(post='Post test',author=self.erass)

    def tearDown(self):
        User.objects.all().delete()
        Neighbourhood.objects.all().delete()
        User.objects.all().delete()
        Post.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))

    def test_save_post(self):
        self.new_post.save_post()
        post =  Post.objects.all()
        self.assertTrue(len(post)>0)



class UserTestClass(TestCase):
    def setUp(self):
        self.new_user=User(username="erass",email="test@gmail.com")
        self.new_user.save()
        self.utawala = Neighbourhood(name='grafix',location='utawala',image='image.jpg',occupants_count=5,admin=self.new_user)
        self.utawala.save_neighborhood()
        self.erass = User(name="mutwech",user=self.new_user,neighborhood=self.utawala)
        self.erass.save()

    def tearDown(self):
        User.objects.all().delete()
        Neighbourhood.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.erass,User))
