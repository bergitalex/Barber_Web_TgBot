from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Master, Visit, Service
from django.views.generic import View, TemplateView, CreateView, DetailView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from .forms import VisitModelForm

class MainView(View):
    def get(self, request, *args, **kwargs):
        masters = Master.objects.all()
        context = {
            'masters': masters,
        }
        return render(request, 'Web/main.html', context)

    def post(self, request, *args, **kwargs):
        name_client = request.POST.get('name')
        phone_client = request.POST.get('phone')
        master_id = request.POST.get('master')
        service_id = request.POST.get('service')
        appointment_date = request.POST.get("appointment_date")
        print('ffffffffffffffffffffffff', appointment_date)
        print(request.POST)
        new_reservation = Visit.objects.create(
            client_name=name_client,
            phone=phone_client,
            master_id=master_id,
            service_id=service_id,
            appointment_date=appointment_date,
        )
        new_reservation.save()
        # редирект на вью ThanksTemplateView
        return redirect('thanks_page')

class VisitListView(ListView):
    model = Visit
    template_name = 'Web/visit_list.html'
    context_object_name = 'visits'

class ThanksTemplateView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'Web/thanks.html')

class VisitCreateView(CreateView):
    model = Visit
    form_class = VisitModelForm  # Форма для создания записи
    template_name = 'Web/visit_form.html'
    success_url = reverse_lazy('visit_list')  # Перенаправление после успешного создания

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Создать'
        return context

class VisitDetailView(DetailView):
    model = Visit
    template_name = 'Web/visit_form.html'  # Используем тот же шаблон
    context_object_name = 'visit'  # Имя объекта для использования в шаблоне

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Просмотр'
        return context

class VisitUpdateView(UpdateView):
    model = Visit
    form_class = VisitModelForm  # Форма для редактирования записи
    template_name = 'Web/visit_form.html'
    success_url = reverse_lazy('visit_list')  # Перенаправление после успешного редактирования

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Редактировать'
        return context

class VisitDeleteView(DeleteView):
    model = Visit
    template_name = 'Web/visit_confirm_delete.html'
    success_url = reverse_lazy('visit_list')  # Перенаправление после удаления

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Удалить'
        return context

# def MainPageView(request):
#     if request.method == "POST":
#         name_client = request.POST.get('name')
#         phone_client = request.POST.get('phone')
#         master_id = request.POST.get('master')
#         service_id = request.POST.get('service')
#         new_reservation = Reservation.objects.create(
#             name=name_client,
#             phone=phone_client,
#             master_id=master_id,
#             service_id=service_id
#         )
#         new_reservation.save()
#         return render(request, 'Web/txpage.html')
#     else:
#         master = Master.objects.all()
#         return render(request, 'Web/main.html', {'masters': master})
#
# def ThxPageView(request):
#     return render(request, 'Web/txpage.html')
#
def ServicePage(request):
    master_id = request.GET.get('master_id')
    master = Master.objects.filter(id=master_id).first()
    if master is not None:
        services = master.services.all()
        services_data = [{'id': service.id, 'name': service.name, 'price': str(service.price)} for service in services]
    else:
        services_data = []
    return JsonResponse({'services': services_data})
