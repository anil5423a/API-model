from rest_framework import serializers
from app.models import *

class EmployeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employe
        fields='__all__'