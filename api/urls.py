from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.TodoListCreate.as_view(), name="todo-list"),
    path('todos/update/<int:pk>/', views.TodoUpdate.as_view(), name='update-todo'),
    path('todos/delete/<int:pk>/', views.TodoDelete.as_view(), name='delete-todo'),
    path('todos/stats/', views.TodoStatsView.as_view(), name='todos-stats')
]