from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from .views import RegisterView, CustomPasswordChangeView, custom_logout_view
from .forms import CustomLoginForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html', form_class=CustomLoginForm), name='login'),
    path('logout/', custom_logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
]

urlpatterns += [
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset_form.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]