from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class IncomeCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="income_categories")

    def __str__(self):
        return self.name
    
class Income(models.Model):
    title = models.CharField(max_length=250)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE, related_name="incomes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="incomes")
    date = models.DateField()