from django.db import models

# Create your models here.
#Models store things in the data base in a specific way

class BlogPost(models.Model):
    title = models.TextField()
    content = models.TextField(null=True, blank=True)