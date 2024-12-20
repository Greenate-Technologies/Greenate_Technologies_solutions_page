from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class CustomUser(AbstractUser):
    key = models.CharField(max_length=19)

    class Meta:
        verbose_name = 'CustomUser'
        verbose_name_plural = 'CustomUsers'

    def __str__(self):
        return self.username


class init_img(models.Model):
    title = models.CharField(max_length=75)
    image = models.ImageField(default= 'image.png', blank= True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class post(models.Model):
    title = models.CharField(max_length=75)
    content = models.TextField()
    image = models.ImageField(default= 'image.png', blank= True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class comment(models.Model):
    Post = models.ForeignKey(post, on_delete= models.CASCADE, related_name='solutions')
    title = models.CharField(max_length=75)
    content = models.TextField()
    image = models.ImageField(default= 'image.png', blank= True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Key(models.Model):
    key = models.CharField(max_length=19)

    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.date)