from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blog')
    date_time = models.DateTimeField()

    def __str__(self):
        return self.title
    
