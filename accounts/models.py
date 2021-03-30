from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class Profile(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE , blank=True , null=True)
    phone_number = models.CharField(max_length=100)
    city = models.ForeignKey('City' , on_delete=models.CASCADE, blank=True , null=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=30)
    cover = models.TextField(max_length=300, blank=True , null=True)
    email = models.EmailField(max_length=100)
    image = models.ImageField(upload_to= "profile/")
    def __str__(self):
        return str(self.user)

@receiver(post_save , sender=User)
def create_user_profile(sender , instance , created , **kwargs):
    if created:
        Profile.objects.create(user=instance)


class City(models.Model):
    name = models.CharField(max_length=50, blank=True , null=True)
    def __str__(self):
        return self.name
    