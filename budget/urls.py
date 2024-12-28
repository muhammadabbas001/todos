from django.urls import path

from . import views

urlpatterns = [
    path('', views.BudgetListCreateAPIView.as_view(), name="list-create"),
    path('<int:pk>/', views.BudgetRetrieveUpdateDestroyAPIView.as_view(), name="retrieve-update-destroy"),
    path('utilization/', views.BudgetUtilizationAPIView.as_view(), name="budget-utilization"),
]