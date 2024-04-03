from django.db import models

# Create your models here.

#simple store lotto draw result for winning numbers
class LottoDraw(models.Model):
    numbers = models.CharField(max_length=255)
    