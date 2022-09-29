from unittest.util import _MAX_LENGTH
from django.db import models
import uuid
# Create your models here.

class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    street = models.CharField(max_length=255, null=False, blank=False)
    neighborhood = models.CharField(max_length=50, null=False, blank=False)
    city = models.Model(max_length=50, null=False, blank=False)
    state = models.Model(max_length=50, null=False, blank=False)
    zipcode = models.CharField(max_length=9, null=False, blank=False)
    complement = models.CharField(max_length=50, null=False, blank=False)

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cpf = models.CharField(max_length=14)
    password = models.CharField()

class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    address = models.ForeignKey()

class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client_referer
    balance
    account_number = models.IntegerField()
    agency
