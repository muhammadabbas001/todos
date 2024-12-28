from rest_framework import serializers

from .models import Expense, ExpenseCategory

class ExpenseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'title', 'amount', 'category', 'description', 'is_recurring', 'date']


class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = ['id', 'name', 'description']


class ExpenseSerializer(serializers.ModelSerializer):
    category = ExpenseCategorySerializer()
    class Meta:
        model = Expense
        fields = ['id', 'title', 'amount', 'category', 'description', 'is_recurring', 'date']