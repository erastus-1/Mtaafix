from django.db import models
from django.db import IntegrityError
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length = 65)
    locations = (
        ('Nairobi', 'Nairobi'),
        ('Thika', 'Thika'),
        ('Utawala', 'Utawala'),
        ('Rongai', 'Rongai'),
        ('Westlands', 'Westlands'),
    )
    loc  = models.CharField(max_length=65, choices=locations)
    occupants = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = 'Location'


    def __str__(self):
        return f"{self.loc} loc"


    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()
        
    @classmethod
    def search_hood(cls, search_term):
        hoods = cls.objects.filter(name__icontains=search_term)
        return hoods



class Profile(models.Model):
    name = models.CharField(max_length = 65, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    hood = models.ForeignKey(Neighbourhood, blank=True, null=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=200)

    def __str__(self):
        return self.name


    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    @classmethod
    def get_by_id(cls,id):
        profile = cls.objects.get(user = id)
        return profile



class Business(models.Model):
    name = models.CharField(max_length = 65)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(Neighbourhood,blank=True, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)


    def __str__(self):
        return self.name


    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def get_biz(cls, hood):
        hoods = Business.objects.filter(hood_id=Neighbourhood)
        return hoods



class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=300)
    hood = models.ForeignKey(Neighbourhood, blank=True,on_delete=models.CASCADE)
    title = models.CharField(max_length = 65)
        
    def __str__(self):
        return self.description



class Join(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    hood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id



class Comments(models.Model):
    comment = models.CharField(max_length = 600)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    def __str__(self):
        return self.comment






