# urls.py
from django.urls import path
from .views import UserRegistrationView  # View ক্লাস নামটা 'View' দিয়ে শেষ করা ভালো

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
]
