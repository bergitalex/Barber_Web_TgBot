from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomRegisterForm, CustomPasswordChangeForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.views import PasswordChangeView

def custom_logout_view(request):
    logout(request) #разлогин
    request.session.flush()
    return redirect('login')

class RegisterView(CreateView):
    form_class = CustomRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy('password_change_done')
    template_name = 'users/password_change.html'