from rest_framework import serializers

from LoginSystem.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'fname',
            'lname',
            'email',
            'mobile',
            'password'
        ]
