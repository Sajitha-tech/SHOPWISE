from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import  post_save
# Create your models here.


class User(AbstractUser):
    phone=models.CharField(max_length=20,unique=True)


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    full_name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.username
    
class Address(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="addresses"
    )
    address_line = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.city}"


def create_profile(sender,instance,created,**kwargs):
    if created and not instance.is_superuser:
        Profile.objects.create(user=instance)

post_save.connect(create_profile,User)






