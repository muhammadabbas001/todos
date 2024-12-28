from django.urls import path

from . import views

urlpatterns = [
    path('', views.IncomeListCreateAPI.as_view(), name="list-create"),
    path('categories/', views.IncomeCategoryListCreateAPI.as_view(), name="list-category-create"),
    path('<int:pk>/', views.IncomeRetrieveUpdateDestroyAPIView.as_view(), name="icom-detail-update-destroy"),
    path('categories/<int:pk>/', views.IncomeCategoryRetrieveUpdateDestroyAPIView.as_view(), name="category-detail-update-destroy"),
]