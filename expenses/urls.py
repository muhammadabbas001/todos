from django.urls import path

from . import views

urlpatterns = [
    path('', views.ExpenseListCreateAPIView.as_view(), name="expense-list-create"),
    path('categories/', views.ExpenseCategoryListCreateAPIView.as_view(), name="expense-category-list-create"),
    path('<int:pk>/', views.ExpenseRetrieveUpdateDestroyAPIView.as_view(), name="expense-retrieve-update-destroy"),
    path('categories/<int:pk>/', views.ExpenseCategoryRetrieveUpdateDestroyAPIView.as_view(), name="expense-retrieve-update-destroy"),
    path('category/<int:category_id>/', views.ExpenseListAPIView.as_view(), name="expense-list"),
    path('recurring/', views.RecurringExpensesView.as_view(), name='recurring-expenses'),
]