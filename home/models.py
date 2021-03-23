from django.db import models


# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    desc=models.TextField()

    def __str__(self):
        return self.name
class Bookings(models.Model):
    name = models.CharField(max_length=100)
    procode = models.CharField(max_length=100)
    username= models.CharField(max_length=100)
    mnumber = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zipp = models.CharField(max_length=100)
    pmode = models.CharField(max_length=100)



    

