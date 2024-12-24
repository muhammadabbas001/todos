from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializer import UserSerializer, TodoSerializer
from .models import Todo

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class TodoListCreate(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(author=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TodoUpdate(generics.UpdateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return Todo.objects.filter(author=self.request.user)
    

class TodoDelete(generics.DestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(author=user)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response({"detail": "You have successfully deleted the todo."}, status= status.HTTP_200_OK)
    

class TodoStatsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        todos = Todo.objects.filter(author=user)
        total_todos = todos.count()
        completed_todos = todos.filter(is_completed=True).count()
        incomplete_todos = total_todos - completed_todos

        return Response({
            "total_todos": total_todos,
            "completed_todos": completed_todos,
            "incomplete_todos": incomplete_todos
        })