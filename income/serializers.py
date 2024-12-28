from rest_framework import serializers

from .models import Income, IncomeCategory

class IncomeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['id', 'title', 'amount', 'description', 'date', 'category']


class IncomeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeCategory
        fields = ['id', 'name', 'description']

        
class IncomeSerializer(serializers.ModelSerializer):
    category = IncomeCategorySerializer()
    class Meta:
        model = Income
        fields = ['id', 'title', 'amount', 'description', 'date', 'category']
