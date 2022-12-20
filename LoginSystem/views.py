from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from LoginSystem.models import *
from LoginSystem.serializers import *
# Create your views here.


class UserSignUpAPIView(APIView):
    """
    USER SIGNUP APIVIEW
    """

    def post(self, request, *args, **kwargs):
        input_data = request.data.copy()
        obj = User(
                    fname=input_data["fname"], 
                    lname=input_data["lname"], 
                    email=input_data["email"], 
                    mobile=input_data["mobile"],
                    password=input_data["password"],
                    is_staff=input_data["is_staff"],
                    is_admin=input_data["is_admin"],)
        obj.save()
        result = {
            "user_id":obj.user_id,
            "fname":obj.fname,
            "lname":obj.lname,
            "email":obj.email,
            "mobile":obj.mobile,
            "is_staff":obj.is_staff,
            "is_admin":obj.is_admin
        }
        result_data = {
            "code" : 201,
            "message" : "User created Successfully!!! ",
            "data":result
        }
        return Response(result_data, 201)

class UserLoginAPIView(APIView):
    """
    USER LOGIN APIVIEW
    """

    def post(self, request, *args, **kwargs):
        input_data = request.data.copy()
        try:
            if ("email" in input_data) and ("password" in input_data):
                obj = User.objects.get(email=input_data["email"])
                srl_obj = UserSerializer(instance=obj)
                if srl_obj.data:
                    if srl_obj.data["password"]==input_data["password"]:
                        result = {
                            "user_id":srl_obj.data["user_id"],
                            "fname":srl_obj.data["fname"],
                            "lname":srl_obj.data["lname"],
                            "email":srl_obj.data["email"],
                            "mobile":srl_obj.data["mobile"],
                            "is_staff":srl_obj.data["is_staff"],
                            "is_admin":srl_obj.data["is_admin"],
                        }
                        result_data = {
                            "code" : 200,
                            "message" : "User Logged In Successfully!!! ",
                            "data":result
                        }
                        return Response(result_data)
                result_data = {
                    "code" : 400,
                    "message" : "Password not Matched!!! ",
                    "data":[]
                }
                return Response(result_data)            
            elif ("mobile" in input_data) and ("password" in input_data):
                obj = User.objects.get(mobile=input_data["mobile"])
                srl_obj = UserSerializer(instance=obj)
                if srl_obj.data:
                    if srl_obj.data["password"]==input_data["password"]:
                        result = {
                            "user_id":srl_obj.data["user_id"],
                            "fname":srl_obj.data["fname"],
                            "lname":srl_obj.data["lname"],
                            "email":srl_obj.data["email"],
                            "mobile":srl_obj.data["mobile"],
                            "is_staff":srl_obj.data["is_staff"],
                            "is_admin":srl_obj.data["is_admin"],
                        }
                        result_data = {
                            "code" : 200,
                            "message" : "User Logged In Successfully!!! ",
                            "data":result
                        }
                        return Response(result_data)
                result_data = {
                    "code" : 400,
                    "message" : "Password not Matched!!! ",
                    "data":[]
                }
                return Response(result_data)  
        except Exception as e:
            result_data = {
                "code" : 400,
                "message" : "User Not Found!!!",
                "data":str(e)
            }
            return Response(result_data)          