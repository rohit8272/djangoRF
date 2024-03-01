from django.db import models

class Students(models.Model):
    name= models.CharField(max_length=100)
    age= models.IntegerField(default=18)
    email = models.EmailField(default="google@goole.com")
    address = models.TextField(default="earth")
   
class Category(models.Model):
    category_name = models.CharField(max_length =100 , default = "engineering")


class Book(models.Model):
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    book_title = models.CharField(max_length=100)