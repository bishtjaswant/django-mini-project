from django.db import models

# Create your models here.
class Post(models.Model):
    title= models.CharField( max_length=50)
    description = models.TextField()
    posted = models.DateTimeField( auto_now=True)
    