from django.db import models
import bcrypt

# Create your models here.

class Users(models.Model):
    salt = bcrypt.gensalt()
    
    email = models.EmailField()
    password = models.CharField(max_length=32)
    salt = models.CharField(max_length=32, default=salt)
    
    def __str__(self):
        return "{}: {}".format(self.pk, self.email)
        
    
    
