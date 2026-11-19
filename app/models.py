from django.db import models

# Create your models here.
class Employee(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    designation = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)