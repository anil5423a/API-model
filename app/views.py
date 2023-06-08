from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from app.models import *

from app.serializers import *
from rest_framework.response import Response
#from rest_framework import status
@api_view()
def Employedata(request):
    EQS=Employe.objects.all()
    ESD=EmployeModelSerializer(EQS,many=True)
    return Response(ESD.data)
