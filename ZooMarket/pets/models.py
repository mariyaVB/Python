from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=1)


class Feedback(models.Model):
    objects = None
    text = models.CharField(max_length=30)
    data_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)


