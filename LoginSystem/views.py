from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *


class DoctorAPIView(APIView):
    """
    CRUD APIS OF DOCTOR MODEL
    """
    def get(self, request, *args, **kwargs):
        """
        READ ONCE DOCTOR API
        """
        obj = Doctor.objects.get(doctor_id=request.query_params.get("doctor_id"))
        srl_obj = DoctorSerializer(instance=obj)
        result = {
            "status": "200",
            "message": "Doctor View Successfully!",
            "data":srl_obj.data
        }
        return Response(result, 200)        

    def post(self, request, *args, **kwargs):
        """
        CREATE DOCTOR API
        """        
        srl_obj=DoctorSerializer(data=request.data)
        if srl_obj.is_valid():
            srl_obj.save()
            result = {
                "status": "201",
                "message": "Doctor Created Successfully!",
                "data":srl_obj.data
            }
            return Response(result, 201)
        else:
            result = {
                "status": "200",
                "message": "Doctor not created!",
                "data":srl_obj.errors
            }
            return Response(result, 200)
    
    def patch(self, request, *args, **kwargs):
        """
        UPDATE DOCTOR API
        """          
        update_data = {}
        if "doctor_name" in request.data:
            update_data["doctor_name"] = request.data["doctor_name"]
        if "doctor_speciality" in request.data:
            update_data["doctor_speciality"] = request.data["doctor_speciality"]
        if "doctor_email" in request.data:
            update_data["doctor_email"] = request.data["doctor_email"]
        if "doctor_mobile" in request.data:
            update_data["doctor_mobile"] = request.data["doctor_mobile"]
        if "doctor_address" in request.data:
            update_data["doctor_address"] = request.data["doctor_address"]
        if "doctor_gender" in request.data:
            update_data["doctor_gender"] = request.data["doctor_gender"]
        if "doctor_license" in request.data:
            update_data["doctor_license"] = request.data["doctor_license"]
        
        obj =  Doctor.objects.get(doctor_id=request.data["doctor_id"])
        srl_obj = DoctorSerializer(instance=obj,data=update_data)
        if srl_obj.is_valid():
            srl_obj.save()
            result = {
                "status": "201",
                "message": "Doctor Updated Successfully!",
                "data":srl_obj.data
            }
            return Response(result, 201)
        else:
            result = {
                "status": "200",
                "message": "Doctor not Updated!",
                "data":srl_obj.errors
            }
            return Response(result, 200)            


    def delete(self, request, *args, **kwargs):  
        """
        DELETE DOCTOR API
        """                
        obj =  Doctor.objects.get(doctor_id=request.query_params.get("doctor_id"))
        obj.delete()
        result = {
            "status": "200",
            "message": "Doctor Deleted Successfully!",
            "data": "Doctor Deleted Successfully!"
        }
        return Response(result, 200) 


class ReadAllDoctorsAPIView(APIView):
    """
    READ ALL DOCTOR API
    """
    def get(self, request, *args, **kwargs):
        """
        READ ALL DOCTOR API
        """
        obj = Doctor.objects.all()
        srl_obj = DoctorSerializer(instance=obj, many=True)
        result = {
            "status": "200",
            "message": "Doctor View Successfully!",
            "data":srl_obj.data
        }
        return Response(result, 200)  



class NurseAPIView(APIView):
    """
    CRUD APIS OF NURSE MODEL
    """
    def get(self, request, *args, **kwargs):
        """
        READ ONCE NURSE API
        """
        obj = Nurse.objects.get(nurse_id=request.query_params.get("nurse_id"))
        srl_obj = NurseSerializer(instance=obj)
        result = {
            "status": "200",
            "message": "Nurse View Successfully!",
            "data":srl_obj.data
        }
        return Response(result, 200)        

    def post(self, request, *args, **kwargs):
        """
        CREATE NURSE API
        """        
        srl_obj=NurseSerializer(data=request.data)
        if srl_obj.is_valid():
            srl_obj.save()
            result = {
                "status": "201",
                "message": "Nurse Created Successfully!",
                "data":srl_obj.data
            }
            return Response(result, 201)
        else:
            result = {
                "status": "200",
                "message": "Nurse not created!",
                "data":srl_obj.errors
            }
            return Response(result, 200)
    
    def patch(self, request, *args, **kwargs):
        """
        UPDATE NURSE API
        """          
        update_data = {}
        if "nurse_name" in request.data:
            update_data["nurse_name"] = request.data["nurse_name"]
        if "nurse_email" in request.data:
            update_data["nurse_email"] = request.data["nurse_email"]
        if "nurse_mobile" in request.data:
            update_data["nurse_mobile"] = request.data["nurse_mobile"]
        if "nurse_address" in request.data:
            update_data["nurse_address"] = request.data["nurse_address"]
        if "nurse_gender" in request.data:
            update_data["nurse_gender"] = request.data["nurse_gender"]
        
        obj =  Nurse.objects.get(nurse_id=request.data["nurse_id"])
        srl_obj = NurseSerializer(instance=obj,data=update_data)
        if srl_obj.is_valid():
            srl_obj.save()
            result = {
                "status": "201",
                "message": "Nurse Updated Successfully!",
                "data":srl_obj.data
            }
            return Response(result, 201)
        else:
            result = {
                "status": "200",
                "message": "Nurse not Updated!",
                "data":srl_obj.errors
            }
            return Response(result, 200)            

    def delete(self, request, *args, **kwargs):  
        """
        DELETE NURSE API
        """                
        obj =  Nurse.objects.get(nurse_id=request.query_params.get("nurse_id"))
        obj.delete()
        result = {
            "status": "200",
            "message": "Nurse Deleted Successfully!",
            "data": "Nurse Deleted Successfully!"
        }
        return Response(result, 200) 


class ReadAllNursesAPIView(APIView):
    """
    READ ALL NURSES API
    """
    def get(self, request, *args, **kwargs):
        """
        READ ALL NURSES API
        """
        obj = Nurse.objects.all()
        srl_obj = NurseSerializer(instance=obj, many=True)
        result = {
            "status": "200",
            "message": "Nurse View Successfully!",
            "data":srl_obj.data
        }
        return Response(result, 200)  



class PatientAPIView(APIView):
    """
    CRUD APIS OF PATIENT MODEL
    """
    def get(self, request, *args, **kwargs):
        """
        READ ONCE PATIENT API
        """
        obj = Patient.objects.get(patient_id=request.query_params.get("patient_id"))
        srl_obj = PatientSerializer(instance=obj)
        result = {
            "status": "200",
            "message": "Patient View Successfully!",
            "data":srl_obj.data
        }
        return Response(result, 200)        

    def post(self, request, *args, **kwargs):
        """
        CREATE PATIENT API
        """        
        srl_obj=PatientSerializer(data=request.data)
        if srl_obj.is_valid():
            srl_obj.save()
            result = {
                "status": "201",
                "message": "Patient Created Successfully!",
                "data":srl_obj.data
            }
            return Response(result, 201)
        else:
            result = {
                "status": "200",
                "message": "Patient not created!",
                "data":srl_obj.errors
            }
            return Response(result, 200)
    
    def patch(self, request, *args, **kwargs):
        """
        UPDATE PATIENT API
        """          
        update_data = {}
        if "patient_name" in request.data:
            update_data["patient_name"] = request.data["patient_name"]
        if "patient_age" in request.data:
            update_data["patient_age"] = request.data["patient_age"]
        if "patient_email" in request.data:
            update_data["patient_email"] = request.data["patient_email"]
        if "patient_mobile" in request.data:
            update_data["patient_mobile"] = request.data["patient_mobile"]
        if "patient_address" in request.data:
            update_data["patient_address"] = request.data["patient_address"]
        if "patient_gender" in request.data:
            update_data["patient_gender"] = request.data["patient_gender"]
        if "patient_blood" in request.data:
            update_data["patient_blood"] = request.data["patient_blood"]
        if "patient_height" in request.data:
            update_data["patient_height"] = request.data["patient_height"]
        if "patient_weight" in request.data:
            update_data["patient_weight"] = request.data["patient_weight"]
        
        obj =  Patient.objects.get(patient_id=request.data["patient_id"])
        srl_obj = PatientSerializer(instance=obj,data=update_data)
        if srl_obj.is_valid():
            srl_obj.save()
            result = {
                "status": "201",
                "message": "Patient Updated Successfully!",
                "data":srl_obj.data
            }
            return Response(result, 201)
        else:
            result = {
                "status": "200",
                "message": "Patient not Updated!",
                "data":srl_obj.errors
            }
            return Response(result, 200)            


    def delete(self, request, *args, **kwargs):  
        """
        DELETE PATIENT API
        """                
        obj =  Patient.objects.get(patient_id=request.query_params.get("patient_id"))
        obj.delete()
        result = {
            "status": "200",
            "message": "Patient Deleted Successfully!",
            "data": "Patient Deleted Successfully!"
        }
        return Response(result, 200) 


class ReadAllPatientsAPIView(APIView):
    """
    READ ALL PATIENTS API
    """
    def get(self, request, *args, **kwargs):
        """
        READ ALL PATIENTS API
        """
        obj = Patient.objects.all()
        srl_obj = PatientSerializer(instance=obj, many=True)
        result = {
            "status": "200",
            "message": "Patient View Successfully!",
            "data":srl_obj.data
        }
        return Response(result, 200)  



class PharmacistAPIView(APIView):
    """
    CRUD APIS OF PHARMACIST MODEL
    """
    def get(self, request, *args, **kwargs):
        """
        READ ONCE PHARMACIST API
        """
        obj = Pharmacist.objects.get(pharmacist_id=request.query_params.get("pharmacist_id"))
        srl_obj = PharmacistSerializer(instance=obj)
        result = {
            "status": "200",
            "message": "Pharmacist View Successfully!",
            "data":srl_obj.data
        }
        return Response(result, 200)        

    def post(self, request, *args, **kwargs):
        """
        CREATE PHARMACIST API
        """        
        srl_obj=PharmacistSerializer(data=request.data)
        if srl_obj.is_valid():
            srl_obj.save()
            result = {
                "status": "201",
                "message": "Pharmacist Created Successfully!",
                "data":srl_obj.data
            }
            return Response(result, 201)
        else:
            result = {
                "status": "200",
                "message": "Pharmacist not created!",
                "data":srl_obj.errors
            }
            return Response(result, 200)
    
    def patch(self, request, *args, **kwargs):
        """
        UPDATE PHARMACIST API
        """          
        update_data = {}
        if "pharmacist_name" in request.data:
            update_data["pharmacist_name"] = request.data["pharmacist_name"]
        if "pharmacist_email" in request.data:
            update_data["pharmacist_email"] = request.data["pharmacist_email"]
        if "pharmacist_mobile" in request.data:
            update_data["pharmacist_mobile"] = request.data["pharmacist_mobile"]
        if "pharmacist_address" in request.data:
            update_data["pharmacist_address"] = request.data["pharmacist_address"]
        if "pharmacist_gender" in request.data:
            update_data["pharmacist_gender"] = request.data["pharmacist_gender"]
        if "pharmacist_license" in request.data:
            update_data["pharmacist_license"] = request.data["pharmacist_license"]
        
        obj =  Pharmacist.objects.get(pharmacist_id=request.data["pharmacist_id"])
        srl_obj = PharmacistSerializer(instance=obj,data=update_data)
        if srl_obj.is_valid():
            srl_obj.save()
            result = {
                "status": "201",
                "message": "Pharmacist Updated Successfully!",
                "data":srl_obj.data
            }
            return Response(result, 201)
        else:
            result = {
                "status": "200",
                "message": "Pharmacist not Updated!",
                "data":srl_obj.errors
            }
            return Response(result, 200)            

    def delete(self, request, *args, **kwargs):  
        """
        DELETE PHARMACIST API
        """                
        obj =  Pharmacist.objects.get(pharmacist_id=request.query_params.get("pharmacist_id"))
        obj.delete()
        result = {
            "status": "200",
            "message": "Pharmacist Deleted Successfully!",
            "data": "Pharmacist Deleted Successfully!"
        }
        return Response(result, 200) 


class ReadAllPharmacistsAPIView(APIView):
    """
    READ ALL PHARMACISTS API
    """
    def get(self, request, *args, **kwargs):
        """
        READ ALL PHARMACISTS API
        """
        obj = Pharmacist.objects.all()
        srl_obj = PharmacistSerializer(instance=obj, many=True)
        result = {
            "status": "200",
            "message": "Pharmacist View Successfully!",
            "data":srl_obj.data
        }
        return Response(result, 200)  



class LabouratoristAPIView(APIView):
    """
    CRUD APIS OF LABOURATORIST MODEL
    """
    def get(self, request, *args, **kwargs):
        """
        READ ONCE LABOURATORIST API
        """
        obj = Labouratorist.objects.get(labouratorist_id=request.query_params.get("labouratorist_id"))
        srl_obj = LabouratoristSerializer(instance=obj)
        result = {
            "status": "200",
            "message": "Labouratorist View Successfully!",
            "data":srl_obj.data
        }
        return Response(result, 200)        

    def post(self, request, *args, **kwargs):
        """
        CREATE LABOURATORIST API
        """        
        srl_obj=LabouratoristSerializer(data=request.data)
        if srl_obj.is_valid():
            srl_obj.save()
            result = {
                "status": "201",
                "message": "Labouratorist Created Successfully!",
                "data":srl_obj.data
            }
            return Response(result, 201)
        else:
            result = {
                "status": "200",
                "message": "Labouratorist not created!",
                "data":srl_obj.errors
            }
            return Response(result, 200)
    
    def patch(self, request, *args, **kwargs):
        """
        UPDATE LABOURATORIST API
        """          
        update_data = {}
        if "labouratorist_name" in request.data:
            update_data["labouratorist_name"] = request.data["labouratorist_name"]
        if "labouratorist_email" in request.data:
            update_data["labouratorist_email"] = request.data["labouratorist_email"]
        if "labouratorist_mobile" in request.data:
            update_data["labouratorist_mobile"] = request.data["labouratorist_mobile"]
        if "labouratorist_address" in request.data:
            update_data["labouratorist_address"] = request.data["labouratorist_address"]
        if "labouratorist_gender" in request.data:
            update_data["labouratorist_gender"] = request.data["labouratorist_gender"]
        if "labouratorist_license" in request.data:
            update_data["labouratorist_license"] = request.data["labouratorist_license"]
        
        obj =  Labouratorist.objects.get(labouratorist_id=request.data["labouratorist_id"])
        srl_obj = LabouratoristSerializer(instance=obj,data=update_data)
        if srl_obj.is_valid():
            srl_obj.save()
            result = {
                "status": "201",
                "message": "Labouratorist Updated Successfully!",
                "data":srl_obj.data
            }
            return Response(result, 201)
        else:
            result = {
                "status": "200",
                "message": "Labouratorist not Updated!",
                "data":srl_obj.errors
            }
            return Response(result, 200)            

    def delete(self, request, *args, **kwargs):  
        """
        DELETE LABOURATORIST API
        """                
        obj =  Labouratorist.objects.get(labouratorist_id=request.query_params.get("labouratorist_id"))
        obj.delete()
        result = {
            "status": "200",
            "message": "Labouratorist Deleted Successfully!",
            "data": "Labouratorist Deleted Successfully!"
        }
        return Response(result, 200) 


class ReadAllLabouratoristsAPIView(APIView):
    """
    READ ALL LABOURATORISTS API
    """
    def get(self, request, *args, **kwargs):
        """
        READ ALL LABOURATORISTS API
        """
        obj = Labouratorist.objects.all()
        srl_obj = LabouratoristSerializer(instance=obj, many=True)
        result = {
            "status": "200",
            "message": "Labouratorist View Successfully!",
            "data":srl_obj.data
        }
        return Response(result, 200)  



class AccountantAPIView(APIView):
    """
    CRUD APIS OF ACCOUNTANT MODEL
    """
    def get(self, request, *args, **kwargs):
        """
        READ ONCE ACCOUNTANT API
        """
        obj = Accountant.objects.get(accountant_id=request.query_params.get("accountant_id"))
        srl_obj = AccountantSerializer(instance=obj)
        result = {
            "status": "200",
            "message": "Accountant View Successfully!",
            "data":srl_obj.data
        }
        return Response(result, 200)        

    def post(self, request, *args, **kwargs):
        """
        CREATE ACCOUNTANT API
        """        
        srl_obj=AccountantSerializer(data=request.data)
        if srl_obj.is_valid():
            srl_obj.save()
            result = {
                "status": "201",
                "message": "Accountant Created Successfully!",
                "data":srl_obj.data
            }
            return Response(result, 201)
        else:
            result = {
                "status": "200",
                "message": "Accountant not created!",
                "data":srl_obj.errors
            }
            return Response(result, 200)
    
    def patch(self, request, *args, **kwargs):
        """
        UPDATE ACCOUNTANT API
        """          
        update_data = {}
        if "accountant_name" in request.data:
            update_data["accountant_name"] = request.data["accountant_name"]
        if "accountant_email" in request.data:
            update_data["accountant_email"] = request.data["accountant_email"]
        if "accountant_mobile" in request.data:
            update_data["accountant_mobile"] = request.data["accountant_mobile"]
        if "accountant_address" in request.data:
            update_data["accountant_address"] = request.data["accountant_address"]
        if "accountant_gender" in request.data:
            update_data["accountant_gender"] = request.data["accountant_gender"]
        
        obj =  Accountant.objects.get(accountant_id=request.data["accountant_id"])
        srl_obj = AccountantSerializer(instance=obj,data=update_data)
        if srl_obj.is_valid():
            srl_obj.save()
            result = {
                "status": "201",
                "message": "Accountant Updated Successfully!",
                "data":srl_obj.data
            }
            return Response(result, 201)
        else:
            result = {
                "status": "200",
                "message": "Accountant not Updated!",
                "data":srl_obj.errors
            }
            return Response(result, 200)            

    def delete(self, request, *args, **kwargs):  
        """
        DELETE ACCOUNTANT API
        """                
        obj =  Accountant.objects.get(accountant_id=request.query_params.get("accountant_id"))
        obj.delete()
        result = {
            "status": "200",
            "message": "Accountant Deleted Successfully!",
            "data": "Accountant Deleted Successfully!"
        }
        return Response(result, 200) 


class ReadAllAccountantsAPIView(APIView):
    """
    READ ALL ACCOUNTANTS API
    """
    def get(self, request, *args, **kwargs):
        """
        READ ALL ACCOUNTANTS API
        """
        obj = Accountant.objects.all()
        srl_obj = AccountantSerializer(instance=obj, many=True)
        result = {
            "status": "200",
            "message": "Accountant View Successfully!",
            "data":srl_obj.data
        }
        return Response(result, 200)  