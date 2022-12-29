from django.urls import path

from .views import *


urlpatterns = [
    #Appointment Urls
    path('appointment/', AppointmentAPIView.as_view(), name='appointment'),
    path('read-all-appointments/', ReadAllAppointmentsAPIView.as_view(), name='read-all-appointments'),    


    #BloodBank Urls
    path('bloodbank/', BloodBankAPIView.as_view(), name='bloodbank'),
    path('read-all-bloodbanks/', ReadAllBloodBanksAPIView.as_view(), name='read-all-bloodbanks'),    
]