from django.db import models
import uuid

# Create your models here.

class Appointment(models.Model):
    appointment_id = models.CharField(max_length=100, default=uuid.uuid4, null=True, blank=True)
    patient_id = models.CharField(max_length=100, null=True, blank=True)
    doctor_id = models.CharField(max_length=100, null=True, blank=True)
    accountant_id = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.CharField(max_length=100, null=True, blank=True)
    end_date = models.CharField(max_length=100, null=True, blank=True)
    amount = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) :
        return str(self.appointment_id)    


class BloodBank(models.Model):
    bloodbank_id = models.CharField(max_length=100, default=uuid.uuid4, null=True, blank=True)
    blood_group = models.CharField(max_length=10, null=True, blank=True)
    donor = models.BooleanField(default=False)
    withdrawer = models.BooleanField(default=False)
    name = models.CharField(max_length=100, null=True, blank=True)
    age = models.CharField(max_length=10, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    patient = models.BooleanField(default=False)
    individual = models.BooleanField(default=False)
    datetime = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) :
        return str(self.bloodbank_id)    