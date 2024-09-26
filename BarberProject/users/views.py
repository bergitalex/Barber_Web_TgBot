from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomRegisterForm
from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout_view(request):
    logout(request) #разлогин
    request.session.flush()
    return redirect('login')

class RegisterView(CreateView):
    form_class = CustomRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

