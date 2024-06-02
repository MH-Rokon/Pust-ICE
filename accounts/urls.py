from django.urls import path
from .views import UserRegistrationView, UserLoginView, user_logout, UserProfileUpdateView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),  # Fix the logout path
    path('profile/', UserProfileUpdateView.as_view(), name='profile'),
]
