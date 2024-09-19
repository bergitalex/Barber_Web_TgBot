from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view()),
    path('thx/', views.ThanksTemplateView.as_view(), name='thanks_page'),
    path('visit/add/', views.VisitCreateView.as_view(), name='visit_create'),
    path('visit/<int:pk>/view/', views.VisitDetailView.as_view(), name='visit_detail'),
    path('visit/<int:pk>/edit/', views.VisitUpdateView.as_view(), name='visit_update'),
    path('visit/<int:pk>/delete/', views.VisitDeleteView.as_view(), name='visit_delete'),
    path('visit/list/', views.VisitListView.as_view(), name='visit_list')
]