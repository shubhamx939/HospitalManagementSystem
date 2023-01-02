from rest_framework import serializers
from .models import *
from LoginSystem.models import *
from LoginSystem.serializers import *


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class BloodBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodBank
        fields = '__all__'


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'


class MedicineSalesSerializer(serializers.ModelSerializer):

    medicine = MedicineSerializer()
    patient = PatientSerializer()
    doctor = DoctorSerializer()
    accountant = AccountantSerializer()
    pharmacist = PharmacistSerializer()

    class Meta:
        model = MedicineSales
        fields = [
            "medicinesales_id",
            "medicine",
            "patient",
            "doctor",
            "accountant",
            "pharmacist",
            "datetime",
        ]