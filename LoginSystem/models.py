from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=70)
    lname = models.CharField(max_length=70)
    email = models.EmailField(max_length=254)
    mobile = models.CharField(max_length=13)
    password = models.CharField(max_length=40, default="")
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return (str(self.email))