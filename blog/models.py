from django.db import models

# Create your models here.
#Models store things in the data base in a specific way

class BlogPost(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)