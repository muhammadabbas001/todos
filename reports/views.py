from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from income.models import Income
from expenses.models import Expense
from income.serializers import IncomeListSerializer
from expenses.serializers import ExpenseListSerializer


class SummaryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        income_query = Income.objects.filter(user = request.user)
        expense_query = Expense.objects.filter(user = request.user)

        if start_date:
            income_query = income_query.filter(date__gte = start_date)
            expense_query = expense_query.filter(date__gte = start_date)

        if end_date:
            income_query = income_query.filter(date__lte = end_date)
            expense_query = expense_query.filter(date__lte = end_date)

        total_income = sum(income.amount for income in income_query)
        total_expenses = sum(expense.amount for expense in expense_query)

        total_income = max(total_income, 0)
        total_expenses = max(total_expenses, 0)

        net_balance = total_income - total_expenses
        net_balance = max(net_balance, 0)

        return Response({
            "total_income": round(total_income, 2),
            "total_expenses": round(total_expenses, 2),
            "net_balance": round(net_balance, 2)
        })


class CategoryReportAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, category_id):
        expenses = Expense.objects.filter(user=request.user, category_id=category_id)
        incomes = Income.objects.filter(user=request.user, category_id=category_id)

        total_expenses = sum(expense.amount for expense in expenses)
        total_income = sum(income.amount for income in incomes)
        net_balance = total_income - total_expenses

        expense_serializer = ExpenseListSerializer(expenses, many=True)
        income_serializer = IncomeListSerializer(incomes, many=True)

        return Response({
            "category_id": category_id,
            "total_income": round(total_income, 2),
            "total_expenses": round(total_expenses, 2),
            "net_balance": round(net_balance, 2),
            "expenses": expense_serializer.data,
            "incomes": income_serializer.data,
        })