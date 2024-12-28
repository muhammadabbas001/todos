from django.db import models
from django.contrib.auth.models import User

class Budget(models.Model):
    name = models.CharField(max_length=250)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="budgets")
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.amount}"
    
    @property
    def duration(self):
        return f"{(self.end_date - self.start_date).days} Days"