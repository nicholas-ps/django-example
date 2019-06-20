from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=50)
    comment = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
