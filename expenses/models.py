from django.db import models
from django.contrib.auth.models import User

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="expense_categories")

    def __str__(self):
        return self.name
    
class Expense(models.Model):
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="expenses")
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE, related_name="expenses")
    description = models.TextField(blank=True, null=True)
    is_recurring = models.BooleanField(default=True)
    date = models.DateField()

    def __str__(self):
        return self.title