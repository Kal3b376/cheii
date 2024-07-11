from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    quantity = models.IntegerField()
    description = models.TextField()


def __str__(self):
    return self.name


class Student(models.Model):
    fullname = models.CharField(max_length=200)
    Email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.fullname

# Fullname,email,medical history,age

class Branch(models.Model):
     name = models.CharField(max_length=200)
     location = models.CharField(max_length=100)
     manager = models.CharField(max_length=100)
     email = models.EmailField()

     def __str__(self):
         return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    message = models.CharField(max_length=100)