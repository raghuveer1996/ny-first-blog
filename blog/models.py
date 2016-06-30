from django.db import models
from django.utils import timezone
from django import forms

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200, default='New Notification')
    text = models.TextField()
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class result(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200, default='')
    technology = models.CharField(max_length=200, default='')
    Version = models.CharField(max_length=200, default='')
    release = models.CharField(max_length=200, default='')
    file1 = models.FileField(null=True,blank=True)
    file2 = models.FileField(null=True,blank=True)
    remarks = models.TextField(max_length=200, default='')
