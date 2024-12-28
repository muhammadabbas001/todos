from rest_framework import serializers

from .models import Budget
from expenses.models import Expense

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'name', 'amount', 'start_date', 'end_date', 'duration']


class BudgetUtilizationSerializer(serializers.ModelSerializer):
    utilization = serializers.SerializerMethodField()

    class Meta:
        model = Budget
        fields = ['id', 'name', 'amount', 'start_date', 'end_date', 'duration', 'utilization']

    def get_utilization(self, obj):
        expenses = Expense.objects.filter(date__gte=obj.start_date, date__lte=obj.end_date)
        total_expenses = sum(expense.amount for expense in expenses)
        utilization_percentage = (total_expenses/obj.amount) * 100 if total_expenses > 0 else 0
        return {
            "total_expenses": total_expenses,
            "utilization_percentage": round(utilization_percentage, 2)
        }