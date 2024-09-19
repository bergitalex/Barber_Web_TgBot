from django import forms
from .models import Visit

class VisitModelForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ['client_name', 'phone', 'master', 'service', 'appointment_date']
        labels = {
            'client_name': 'Имя клиента',
            'phone': 'Телефон',
            'master': 'Мастер',
            'service': 'Сервис',
            'appointment_date': 'Дата записи',
        }
        widgets = {
            'appointment_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
