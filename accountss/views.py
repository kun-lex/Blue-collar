from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView


class SignUpView(generic.CreateView):
    form_class = UserCreationForm    
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class PasswordView(TemplateView):
    success_url = reverse_lazy('change_password_done')
    template_name = 'registration/change_password.html'

# Create your views here.
