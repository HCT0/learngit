from django.db import models

# Create your models here.
class passage(models.Model):
    title = models.CharField(max_length=10)
    body = models.CharField(max_length=1000)
    kind = models.CharField(max_length=1000)
    viewer = models.CharField(max_length=1000)

class comment(models.Model):
    user_name = models.CharField(max_length=1000)
    user_comment = models.CharField(max_length=1000)
    passage_class = models.CharField(max_length=1000)

