from django.db import models

# Create your models here.
class Bookmarks(models.Model):
    Link = models.CharField(max_length=200)
    Title = models.CharField(max_length=200)
    Time_Created = models.DateTimeField(auto_now_add=True)
    Publisher = models.CharField(max_length=200)
    Tags = models.CharField(max_length=200)
    def __str__(self):
        return self.Title
class tags(models.Model):
    tag_id = models.CharField(max_length=200,default="")
    Title = models.CharField(max_length=200,default="")
    Time_Created = models.DateTimeField(auto_now_add=True)