from django.db import models

# Create your models here.
class Adult(models.Model):
    adults= models.IntegerField()


class Children(models.Model):
    children= models.IntegerField()

class People(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    adults = models.ForeignKey(Adult, on_delete= models.CASCADE)
    children = models.ForeignKey(Children, on_delete= models.CASCADE)