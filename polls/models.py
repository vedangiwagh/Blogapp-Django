from django.db import models

# Create your models here.


class Post(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    post = models.CharField(max_length=500)
    publish_date = models.DateTimeField('date published')


