from django.db import models

# Create your models here.

class Address(models.Model):
    street = models.CharField(max_length=255, null=False, blank=False)
    neighborhood = models.CharField(max_length=50, null=False, blank=False)
    city = models.Model(max_length=50, null=False, blank=False)
    state = models.Model(max_length=50, null=False, blank=False)
    zipcode = models.CharField(max_length=9, null=False, blank=False)
    complement = models.CharField(max_length=50, null=False, blank=False)

class Client(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    address = models.ForeignKey()
