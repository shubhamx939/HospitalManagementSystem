from django.db import models
import uuid

class Doctor(models.Model):
    doctor_id = models.CharField(max_length=100, default=uuid.uuid4, primary_key=True)
    doctor_name = models.CharField(max_length=50, null=True, blank=True)
    doctor_speciality = models.CharField(max_length=100, null=True, blank=True)
    doctor_email = models.CharField(max_length=50, null=True, blank=True)
    doctor_mobile = models.CharField(max_length=15, null=True, blank=True)
    doctor_address = models.CharField(max_length=150, null=True, blank=True)
    doctor_gender = models.CharField(max_length=10, null=True, blank=True)
    doctor_license = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.doctor_id)


class Nurse(models.Model):
    nurse_id = models.CharField(max_length=100, default=uuid.uuid4, primary_key=True)
    nurse_name = models.CharField(max_length=50, null=True, blank=True)
    nurse_email = models.CharField(max_length=50, null=True, blank=True)
    nurse_mobile = models.CharField(max_length=15, null=True, blank=True)
    nurse_address = models.CharField(max_length=150, null=True, blank=True)
    nurse_gender = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.nurse_id)        


class Patient(models.Model):
    patient_id = models.CharField(max_length=100, default=uuid.uuid4, primary_key=True)
    patient_name = models.CharField(max_length=50, null=True, blank=True)
    patient_age = models.CharField(max_length=10, null=True, blank=True)
    patient_email = models.CharField(max_length=50, null=True, blank=True)
    patient_mobile = models.CharField(max_length=15, null=True, blank=True)
    patient_address = models.CharField(max_length=150, null=True, blank=True)
    patient_gender = models.CharField(max_length=10, null=True, blank=True)
    patient_blood = models.CharField(max_length=10, null=True, blank=True)
    patient_height = models.CharField(max_length=10, null=True, blank=True)
    patient_weight = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.patient_id)        


class Pharmacist(models.Model):
    pharmacist_id = models.CharField(max_length=100, default=uuid.uuid4, primary_key=True)
    pharmacist_name = models.CharField(max_length=50, null=True, blank=True)
    pharmacist_email = models.CharField(max_length=50, null=True, blank=True)
    pharmacist_mobile = models.CharField(max_length=15, null=True, blank=True)
    pharmacist_address = models.CharField(max_length=150, null=True, blank=True)
    pharmacist_gender = models.CharField(max_length=10, null=True, blank=True)
    pharmacist_license = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.pharmacist_id) 


class Labouratorist(models.Model):
    labouratorist_id = models.CharField(max_length=100, default=uuid.uuid4, primary_key=True)
    labouratorist_name = models.CharField(max_length=50, null=True, blank=True)
    labouratorist_email = models.CharField(max_length=50, null=True, blank=True)
    labouratorist_mobile = models.CharField(max_length=15, null=True, blank=True)
    labouratorist_address = models.CharField(max_length=150, null=True, blank=True)
    labouratorist_gender = models.CharField(max_length=10, null=True, blank=True)
    labouratorist_license = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.labouratorist_id) 


class Accountant(models.Model):
    accountant_id = models.CharField(max_length=100, default=uuid.uuid4, primary_key=True)
    accountant_name = models.CharField(max_length=50, null=True, blank=True)
    accountant_email = models.CharField(max_length=50, null=True, blank=True)
    accountant_mobile = models.CharField(max_length=15, null=True, blank=True)
    accountant_address = models.CharField(max_length=150, null=True, blank=True)
    accountant_gender = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.accountant_id) 
