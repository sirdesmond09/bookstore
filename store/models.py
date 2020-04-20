from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.last_name}  {self.first_name}"


    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author)
    description = models.TextField()
    date_posted = models.DateField(default = timezone.now)
    price = models.DecimalField(decimal_places= 2, max_digits= 8)
    stock = models.IntegerField(default=0)


class Review(models.Model):
    book = models.ForeignKey(Book)
    user = models.ForeignKey(User)
    publish_date = models.DateField(default = timezone.now)
    text = models.TextField()