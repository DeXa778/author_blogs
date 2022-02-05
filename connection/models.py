from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=255)
    message = models.TextField()

class Social(models.Model):
    name = models.CharField(max_length=120)
    link = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)


class MenuItem(models.Model):
     name = models.CharField(max_length=120)
     link = models.CharField(max_length=255)
