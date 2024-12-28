from django.urls import path

from .views import SummaryAPIView, CategoryReportAPIView

urlpatterns = [
    path('summary/', SummaryAPIView.as_view(), name="reports-summary"),
    path('category/<int:category_id>', CategoryReportAPIView.as_view(), name="category-based-report"),
]