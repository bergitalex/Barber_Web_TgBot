from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView
from .forms import CustomLoginForm

from .views import custom_logout_view

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html', form_class=CustomLoginForm), name='login'),
    path('logout/', custom_logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
