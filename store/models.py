from django.db import models
from django.utils import timezone

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length= 200)
    description = models.TextField()
    date_posted = models.DateField(default = timezone.now)
    price = models.DecimalField(decimal_places= 2, max_digits= 8)
    stock = models.IntegerField(default=0)