from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()


    def __str__(self) -> str:
        return self.title
    

class Contact(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    phone = models.CharField(max_length=200)
    email = models.EmailField()


    def __str__(self) -> str:
        return self.name
    
