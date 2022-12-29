from rest_framework import serializers
from .models import *

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class PharmacistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacist
        fields = '__all__'


class LabouratoristSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labouratorist
        fields = '__all__'


class AccountantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accountant
        fields = '__all__'