from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from . import serializers
from .models import Income, IncomeCategory

class IncomeListCreateAPI(generics.ListCreateAPIView):
    serializer_class = serializers.IncomeListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Income.objects.filter(user = self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)
    

class IncomeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.IncomeSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return Income.objects.filter(user = self.request.user)


class IncomeCategoryListCreateAPI(generics.ListCreateAPIView):
    serializer_class = serializers.IncomeCategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return IncomeCategory.objects.filter(user = self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)
    

class IncomeCategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.IncomeCategorySerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return IncomeCategory.objects.filter(user = self.request.user)