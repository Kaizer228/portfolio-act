from django.db import models

# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    image = models.CharField(max_length=200)


 