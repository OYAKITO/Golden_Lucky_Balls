from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    coins = models.IntegerField()
    def __str__(self) -> str:
        return self.username
    
    