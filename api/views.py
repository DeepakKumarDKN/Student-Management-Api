from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student, Institute

from api import serializers

from rest_framework.generics import (
  ListAPIView,
  RetrieveAPIView,
  UpdateAPIView,
  RetrieveUpdateAPIView,
  ListCreateAPIView,
  DestroyAPIView
  )

class StudentListView(ListAPIView):
  queryset = Student.objects.all()
  serializer_class = serializers.StudentSerializer
  

class StudentListCreateView(ListCreateAPIView):
  queryset = Student.objects.all()
  serializer_class = serializers.StudentSerializer
  
class StudentDetailView(RetrieveAPIView):
  queryset = Student.objects.all()
  serializer_class = serializers.StudentSerializer


class StudentUpdateView(RetrieveUpdateAPIView):
  queryset = Student.objects.all()
  serializer_class = serializers.StudentSerializer
  
  
class StudentDeleteView(DestroyAPIView):
  queryset = Student.objects.all()
  serializer_class = serializers.StudentSerializer
  
