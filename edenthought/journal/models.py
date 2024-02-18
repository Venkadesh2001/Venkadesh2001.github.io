from django.db import models
from django.contrib.auth.models import User


class CreateThought(models.Model):
        title = models.CharField(max_length = 100)
        description = models.CharField(max_length=400)
        date_created = models.DateTimeField(auto_now_add=True)
        user = models.ForeignKey(User,on_delete=models.CASCADE)


class Profile(models.Model):
        profile_pic = models.ImageField(null=True,blank=True,default = 'Default.png')
        user = models.ForeignKey(User,on_delete=models.CASCADE)
