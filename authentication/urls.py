from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import CreateUserView, PasswordUpdateView

urlpatterns = [
    path('register/', CreateUserView.as_view(), name="register"),
    path('token/', TokenObtainPairView.as_view(), name="get_token"),
    path('token/refresh/', TokenRefreshView.as_view(), name="refresh"),
    path('password-update/', PasswordUpdateView.as_view(), name='password-update'),
    path('', include('rest_framework.urls')),
]