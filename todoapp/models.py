from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=50, blank=True, null=True)
