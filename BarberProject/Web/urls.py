from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPageView, name='main'),
    path('thx/', views.ThxPageView, name='thx'),
    path('services/', views.ServicePage, name='service')
]