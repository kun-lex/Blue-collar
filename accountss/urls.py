from django.urls import path
from .views import SignUpView, PasswordView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('change_password/', PasswordView.as_view(), name = 'change_password')
]
