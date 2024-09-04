from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Master, Reservation

def MainPageView(request):
    if request.method == "POST":
        name_client = request.POST.get('name')
        phone_client = request.POST.get('phone')
        master_id = request.POST.get('master')
        service_id = request.POST.get('service')
        new_reservation = Reservation.objects.create(
            name=name_client,
            phone=phone_client,
            master_id=master_id,
            service_id=service_id
        )
        new_reservation.save()
        return render(request, 'Web/txpage.html')
    else:
        master = Master.objects.all()
        return render(request, 'Web/main.html', {'masters': master})

def ThxPageView(request):
    return render(request, 'Web/txpage.html')

def ServicePage(request):
    master_id = request.GET.get('master_id')
    master = Master.objects.filter(id=master_id).first()
    if master is not None:
        services = master.services.all()
        services_data = [{'id': service.id, 'name': service.name, 'price': str(service.price)} for service in services]
    else:
        services_data = []
    return JsonResponse({'services': services_data})
