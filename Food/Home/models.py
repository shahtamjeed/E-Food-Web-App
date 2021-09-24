from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    image_url = models.CharField(max_length=250)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site=models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)
    def __str__(self):
        return self.user.username
