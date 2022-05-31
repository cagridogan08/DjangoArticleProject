from email.policy import default
from django.db import models
from django.contrib.auth.models import User 
from datetime import datetime
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_date = models.DateField(default=datetime.now)
    image = models.ImageField(upload_to='images',default='blank-article-picture.png')
    edited = models.BooleanField(default=False)
    edit_date = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.title+'/'+ self.author.username
    
    