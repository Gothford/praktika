from django.db import models

# Create your models here.

# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)


class New(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256)
    content = models.TextField()
