from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from  .serializers import *
# Create your views here.

class std_view(viewsets.ModelViewSet):
    queryset=student.objects.all()
    serializer_class=std
