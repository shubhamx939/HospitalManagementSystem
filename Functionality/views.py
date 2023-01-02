from rest_framework.views import APIView
from rest_framework.response import Response
import datetime

from .models import *
from .serializers import *

# Create your views here.
class AppointmentAPIView(APIView):
    """
    CRUD APIS OF APPOINTMENT MODEL
    """
    def get(self, request, *args, **kwargs):
        """
        READ ONCE APPOINTMENT API
        """
        obj = Appointment.objects.get(appointment_id=request.query_params.get("appointment_id"))
        srl_obj = AppointmentSerializer(instance=obj)
        result = {
            "status": "200",
            "message": "Appointment View Successfully!",
            "data":srl_obj.data
        }
        return Response(result, 200)        

    def post(self, request, *args, **kwargs):
        """
        CREATE APPOINTMENT API
        """        
        srl_obj=AppointmentSerializer(data=request.data)
        if srl_obj.is_valid():
            srl_obj.save()
            result = {
                "status": "201",
                "message": "Appointment Created Successfully!",
                "data":srl_obj.data
            }
            return Response(result, 201)
        else:
            result = {
                "status": "200",
                "message": "Appointment not created!",
                "data":srl_obj.errors
            }
            return Response(result, 200)
    
    def patch(self, request, *args, **kwargs):
        """
        UPDATE APPOINTMENT API
        """          
        update_data = {}
        if "patient_id" in request.data:
            update_data["patient_id"] = request.data["patient_id"]
        if "doctor_id" in request.data:
            update_data["doctor_id"] = request.data["doctor_id"]
        if "accountant_id" in request.data:
            update_data["accountant_id"] = request.data["accountant_id"]
        if "start_date" in request.data:
            update_data["start_date"] = request.data["start_date"]
        if "end_date" in request.data:
            update_data["end_date"] = request.data["end_date"]
        if "amount" in request.data:
            update_data["amount"] = request.data["amount"]
        
        obj =  Appointment.objects.get(appointment_id=request.data["appointment_id"])
        srl_obj = AppointmentSerializer(instance=obj,data=update_data)
        if srl_obj.is_valid():
            srl_obj.save()
            result = {
                "status": "201",
                "message": "Appointment Updated Successfully!",
                "data":srl_obj.data
            }
            return Response(result, 201)
        else:
            result = {
                "status": "200",
                "message": "Appointment not Updated!",
                "data":srl_obj.errors
            }
            return Response(result, 200)            


    def delete(self, request, *args, **kwargs):  
        """
        DELETE APPOINTMENT API
        """                
        obj =  Appointment.objects.get(appointment_id=request.query_params.get("appointment_id"))
        obj.delete()
        result = {
            "status": "200",
            "message": "Appointment Deleted Successfully!",
            "data": "Appointment Deleted Successfully!"
        }
        return Response(result, 200) 


class ReadAllAppointmentsAPIView(APIView):
    """
    READ ALL APPOINTMENTS API
    """
    def get(self, request, *args, **kwargs):
        """
        READ ALL APPOINTMENTS API
        """
        obj = Appointment.objects.all()
        srl_obj = AppointmentSerializer(instance=obj, many=True)
        result = {
            "status": "200",
            "message": "Appointment View Successfully!",
            "data":srl_obj.data
        }
        return Response(result, 200)  



class BloodBankAPIView(APIView):
    """
    CRUD APIS OF BLOODBANK MODEL
    """
    def get(self, request, *args, **kwargs):
        """
        READ ONCE BLOODBANK API
        """
        obj = BloodBank.objects.get(bloodbank_id=request.query_params.get("bloodbank_id"))
        srl_obj = BloodBankSerializer(instance=obj)
        result = {
            "status": "200",
            "message": "BloodBank View Successfully!",
            "data":srl_obj.data
        }
        return Response(result, 200)        

    def post(self, request, *args, **kwargs):
        """
        CREATE BLOODBANK API
        """        
        now = datetime.datetime.now()
        request.data["datetime"] = now
        srl_obj=BloodBankSerializer(data=request.data)
        if srl_obj.is_valid():
            srl_obj.save()
            result = {
                "status": "201",
                "message": "BloodBank Created Successfully!",
                "data":srl_obj.data
            }
            return Response(result, 201)
        else:
            result = {
                "status": "200",
                "message": "BloodBank not created!",
                "data":srl_obj.errors
            }
            return Response(result, 200)
    
    def patch(self, request, *args, **kwargs):
        """
        UPDATE BLOODBANK API
        """          
        update_data = {}
        if "blood_group" in request.data:
            update_data["blood_group"] = request.data["blood_group"]
        if "donor" in request.data:
            update_data["donor"] = request.data["donor"]
        if "withdrawer" in request.data:
            update_data["withdrawer"] = request.data["withdrawer"]
        if "age" in request.data:
            update_data["age"] = request.data["age"]
        if "gender" in request.data:
            update_data["gender"] = request.data["gender"]
        if "mobile" in request.data:
            update_data["mobile"] = request.data["mobile"]
        if "patient" in request.data:
            update_data["patient"] = request.data["patient"]
        if "individual" in request.data:
            update_data["individual"] = request.data["individual"]
        
        obj =  BloodBank.objects.get(bloodbank_id=request.data["bloodbank_id"])
        srl_obj = BloodBankSerializer(instance=obj,data=update_data)
        if srl_obj.is_valid():
            srl_obj.save()
            result = {
                "status": "201",
                "message": "BloodBank Updated Successfully!",
                "data":srl_obj.data
            }
            return Response(result, 201)
        else:
            result = {
                "status": "200",
                "message": "BloodBank not Updated!",
                "data":srl_obj.errors
            }
            return Response(result, 200)            


    def delete(self, request, *args, **kwargs):  
        """
        DELETE BLOODBANK API
        """                
        obj =  BloodBank.objects.get(bloodbank_id=request.query_params.get("bloodbank_id"))
        obj.delete()
        result = {
            "status": "200",
            "message": "BloodBank Deleted Successfully!",
            "data": "BloodBank Deleted Successfully!"
        }
        return Response(result, 200) 


class ReadAllBloodBanksAPIView(APIView):
    """
    READ ALL BLOODBANKS API
    """
    def get(self, request, *args, **kwargs):
        """
        READ ALL BLOODBANKS API
        """
        obj = BloodBank.objects.all()
        srl_obj = BloodBankSerializer(instance=obj, many=True)
        result = {
            "status": "200",
            "message": "BloodBank View Successfully!",
            "data":srl_obj.data
        }
        return Response(result, 200)  



class MedicineAPIView(APIView):
    """
    CRUD APIS OF MEDICINE MODEL
    """
    def get(self, request, *args, **kwargs):
        """
        READ ONCE MEDICINE API
        """
        obj = Medicine.objects.get(bloodbank_id=request.query_params.get("bloodbank_id"))
        srl_obj = MedicineSerializer(instance=obj)
        result = {
            "status": "200",
            "message": "Medicine View Successfully!",
            "data":srl_obj.data
        }
        return Response(result, 200)        

    def post(self, request, *args, **kwargs):
        """
        CREATE MEDICINE API
        """        
        srl_obj=MedicineSerializer(data=request.data)
        if srl_obj.is_valid():
            srl_obj.save()
            result = {
                "status": "201",
                "message": "Medicine Created Successfully!",
                "data":srl_obj.data
            }
            return Response(result, 201)
        else:
            result = {
                "status": "200",
                "message": "Medicine not created!",
                "data":srl_obj.errors
            }
            return Response(result, 200)
     
#     def patch(self, request, *args, **kwargs):
#         """
#         UPDATE MEDICINE API
#         """          
#         update_data = {}
#         if "blood_group" in request.data:
#             update_data["blood_group"] = request.data["blood_group"]
#         if "donor" in request.data:
#             update_data["donor"] = request.data["donor"]
#         if "withdrawer" in request.data:
#             update_data["withdrawer"] = request.data["withdrawer"]
#         if "age" in request.data:
#             update_data["age"] = request.data["age"]
#         if "gender" in request.data:
#             update_data["gender"] = request.data["gender"]
#         if "mobile" in request.data:
#             update_data["mobile"] = request.data["mobile"]
#         if "patient" in request.data:
#             update_data["patient"] = request.data["patient"]
#         if "individual" in request.data:
#             update_data["individual"] = request.data["individual"]
        
#         obj =  Medicine.objects.get(bloodbank_id=request.data["bloodbank_id"])
#         srl_obj = MedicineSerializer(instance=obj,data=update_data)
#         if srl_obj.is_valid():
#             srl_obj.save()
#             result = {
#                 "status": "201",
#                 "message": "BloodBank Updated Successfully!",
#                 "data":srl_obj.data
#             }
#             return Response(result, 201)
#         else:
#             result = {
#                 "status": "200",
#                 "message": "BloodBank not Updated!",
#                 "data":srl_obj.errors
#             }
#             return Response(result, 200)            


#     def delete(self, request, *args, **kwargs):  
#         """
#         DELETE MEDICINE API
#         """                
#         obj =  BloodBank.objects.get(bloodbank_id=request.query_params.get("bloodbank_id"))
#         obj.delete()
#         result = {
#             "status": "200",
#             "message": "BloodBank Deleted Successfully!",
#             "data": "BloodBank Deleted Successfully!"
#         }
#         return Response(result, 200) 


# class ReadAllBloodBanksAPIView(APIView):
#     """
#     READ ALL MEDICINE API
#     """
#     def get(self, request, *args, **kwargs):
#         """
#         READ ALL BLOODBANKS API
#         """
#         obj = BloodBank.objects.all()
#         srl_obj = BloodBankSerializer(instance=obj, many=True)
#         result = {
#             "status": "200",
#             "message": "BloodBank View Successfully!",
#             "data":srl_obj.data
#         }
#         return Response(result, 200)  



class MedicineSalesAPIView(APIView):
    """
    CRUD APIS OF MEDICINESALES MODEL
    """
    def get(self, request, *args, **kwargs):
        """
        READ ONCE MEDICINESALES API
        """
        obj = MedicineSales.objects.get(medicinesales_id=request.query_params.get("medicinesales_id"))
        srl_obj = MedicineSalesSerializer(instance=obj)
        result = {
            "status": "200",
            "message": "MedicineSales View Successfully!",
            "data":srl_obj.data
        }
        return Response(result, 200)        

    def post(self, request, *args, **kwargs):
        """
        CREATE MEDICINESALES API
        """        
        now = datetime.datetime.now()
        med_obj = Medicine.objects.get(medicine_id=request.data["medicine_id"])
        med_srl_obj = MedicineSerializer(med_obj)
        patient_obj = Patient.objects.get(patient_id=request.data["patient_id"])
        patient_srl_obj = PatientSerializer(patient_obj)
        doctor_obj = Doctor.objects.get(doctor_id=request.data["doctor_id"])
        doctor_srl_obj = DoctorSerializer(doctor_obj)
        accountant_obj = Accountant.objects.get(accountant_id=request.data["accountant_id"])
        accountant_srl_obj = AccountantSerializer(accountant_obj)
        pharmacist_obj = Pharmacist.objects.get(pharmacist_id=request.data["pharmacist_id"])
        pharmacist_srl_obj = PharmacistSerializer(pharmacist_obj)

        new_data = {
            "datetime": str(now),
            "medicine": med_srl_obj.data,
            "patient": patient_srl_obj.data,
            "doctor": doctor_srl_obj.data,
            "accountant": accountant_srl_obj.data,
            "pharmacist": pharmacist_srl_obj.data
        }
        
        srl_obj=MedicineSalesSerializer(data=new_data)
        if srl_obj.is_valid():
            srl_obj.save()
            result = {
                "status": "201",
                "message": "MedicineSales Created Successfully!",
                "data":srl_obj.data
            }
            return Response(result, 201)
        else:
            result = {
                "status": "200",
                "message": "MedicineSales not created!",
                "data":srl_obj.errors
            }
            return Response(result, 200)
     
#     def patch(self, request, *args, **kwargs):
#         """
#         UPDATE MEDICINESALES API
#         """          
#         update_data = {}
#         if "blood_group" in request.data:
#             update_data["blood_group"] = request.data["blood_group"]
#         if "donor" in request.data:
#             update_data["donor"] = request.data["donor"]
#         if "withdrawer" in request.data:
#             update_data["withdrawer"] = request.data["withdrawer"]
#         if "age" in request.data:
#             update_data["age"] = request.data["age"]
#         if "gender" in request.data:
#             update_data["gender"] = request.data["gender"]
#         if "mobile" in request.data:
#             update_data["mobile"] = request.data["mobile"]
#         if "patient" in request.data:
#             update_data["patient"] = request.data["patient"]
#         if "individual" in request.data:
#             update_data["individual"] = request.data["individual"]
        
#         obj =  Medicine.objects.get(bloodbank_id=request.data["bloodbank_id"])
#         srl_obj = MedicineSerializer(instance=obj,data=update_data)
#         if srl_obj.is_valid():
#             srl_obj.save()
#             result = {
#                 "status": "201",
#                 "message": "BloodBank Updated Successfully!",
#                 "data":srl_obj.data
#             }
#             return Response(result, 201)
#         else:
#             result = {
#                 "status": "200",
#                 "message": "BloodBank not Updated!",
#                 "data":srl_obj.errors
#             }
#             return Response(result, 200)            


#     def delete(self, request, *args, **kwargs):  
#         """
#         DELETE MEDICINESALES API
#         """                
#         obj =  BloodBank.objects.get(bloodbank_id=request.query_params.get("bloodbank_id"))
#         obj.delete()
#         result = {
#             "status": "200",
#             "message": "BloodBank Deleted Successfully!",
#             "data": "BloodBank Deleted Successfully!"
#         }
#         return Response(result, 200) 


# class ReadAllBloodBanksAPIView(APIView):
#     """
#     READ ALL MEDICINESALES API
#     """
#     def get(self, request, *args, **kwargs):
#         """
#         READ ALL MEDICINESALES API
#         """
#         obj = BloodBank.objects.all()
#         srl_obj = BloodBankSerializer(instance=obj, many=True)
#         result = {
#             "status": "200",
#             "message": "BloodBank View Successfully!",
#             "data":srl_obj.data
#         }
#         return Response(result, 200)  
