from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    rating = models.PositiveIntegerField(default=settings.DEFAULT_USER_RATING)

class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline
