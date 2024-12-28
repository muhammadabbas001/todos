from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .serializers import ExpenseSerializer, ExpenseCategorySerializer, ExpenseListSerializer
from .models import Expense, ExpenseCategory

class ExpenseListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ExpenseListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ExpenseListAPIView(generics.ListAPIView):
    serializer_class = ExpenseListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return Expense.objects.filter(user=self.request.user, category_id=category_id)


class ExpenseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)
    

class RecurringExpensesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        recurring_expenses = Expense.objects.filter(user=request.user, is_recurring=True)
        serializer = ExpenseSerializer(recurring_expenses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ExpenseCategoryListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ExpenseCategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ExpenseCategory.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ExpenseCategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseCategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ExpenseCategory.objects.filter(user=self.request.user)