from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    def __str__(self):
        return f'{ self.title}'
    
