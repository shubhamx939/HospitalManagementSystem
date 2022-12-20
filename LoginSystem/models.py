from django.db import models
from uuid import uuid4

# Create your models here.

class User(models.Model):
    id = models.UUIDField(default=uuid4(), primary_key=True)
    fname = models.CharField(max_length=70)
    lname = models.CharField(max_length=70)
    email = models.EmailField(max_length=254)
    mobile = models.CharField(max_length=13)
    password = models.CharField(max_length=40, default="")

    def __str__(self):
        return (str(self.id))