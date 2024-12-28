from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Budget
from .serializers import BudgetSerializer, BudgetUtilizationSerializer

class BudgetListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Budget.objects.filter(user = self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)
    

class BudgetRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return Budget.objects.filter(user = self.request.user)
    

class BudgetUtilizationAPIView(generics.ListAPIView):
    serializer_class = BudgetUtilizationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Budget.objects.filter(user = self.request.user)