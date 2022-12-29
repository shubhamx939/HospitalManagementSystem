from django.urls import path
from .views import *

urlpatterns = [
    #Doctor Urls
    path('doctor/', DoctorAPIView.as_view(), name='doctor'),
    path('read-all-doctors/', ReadAllDoctorsAPIView.as_view(), name='read-all-doctors'),

    #Nurse Urls
    path('nurse/', NurseAPIView.as_view(), name='nurse'),
    path('read-all-nurses/', ReadAllNursesAPIView.as_view(), name='read-all-nurses'),

    #Patients Urls
    path('patient/', PatientAPIView.as_view(), name='patient'),
    path('read-all-patients/', ReadAllPatientsAPIView.as_view(), name='read-all-patients'),

    #Pharmacist Urls
    path('pharmacist/', PharmacistAPIView.as_view(), name='pharmacist'),
    path('read-all-pharmacists/', ReadAllPharmacistsAPIView.as_view(), name='read-all-pharmacists'),

    #Labouratorist Urls
    path('labouratorist/', LabouratoristAPIView.as_view(), name='labouratorist'),
    path('read-all-labouratorists/', ReadAllLabouratoristsAPIView.as_view(), name='read-all-labouratorists'),

    #Accountant Urls
    path('accountant/', AccountantAPIView.as_view(), name='accountant'),
    path('read-all-accountants/', ReadAllAccountantsAPIView.as_view(), name='read-all-accountants'),
]