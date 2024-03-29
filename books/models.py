from django.db import models

# Create your models here.
class Author(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    
class Book(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13)



    