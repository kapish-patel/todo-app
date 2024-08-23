from django.db import models

# Create your models here.

class Todo(models.Model):
    userId = models.PositiveIntegerField()
    description = models.TextField()
    todobucketid = models.PositiveIntegerField(default=1)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.description