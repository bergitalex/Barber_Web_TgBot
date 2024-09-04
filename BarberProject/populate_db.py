import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BarberProject.settings')
django.setup()

from Web.models import Master, Service

def create_services():
    services_data = [
        {"name": "Стрижка", "price": 1500.00},
        {"name": "Бритье", "price": 1200.00},
        {"name": "Укладка", "price": 1000.00},
        {"name": "Массаж головы", "price": 800.00},
        {"name": "Маникюр", "price": 500.00},
    ]

    services = []
    for service_data in services_data:
        service, created = Service.objects.get_or_create(
            name=service_data["name"],
            price=service_data["price"]
        )
        services.append(service)
    return services

def create_masters(services):
    masters_data = [
        {"first_name": "Алексей", "last_name": "Иванов", "contact_info": "email1@example.com"},
        {"first_name": "Михаил", "last_name": "Петров", "contact_info": "email2@example.com"},
        {"first_name": "Сергей", "last_name": "Сидоров", "contact_info": "email3@example.com"},
        {"first_name": "Владимир", "last_name": "Кузнецов", "contact_info": "email4@example.com"},
        {"first_name": "Дмитрий", "last_name": "Смирнов", "contact_info": "email5@example.com"},
        {"first_name": "Андрей", "last_name": "Васильев", "contact_info": "email6@example.com"},
        {"first_name": "Евгений", "last_name": "Павлов", "contact_info": "email7@example.com"},
        {"first_name": "Иван", "last_name": "Романов", "contact_info": "email8@example.com"},
        {"first_name": "Николай", "last_name": "Козлов", "contact_info": "email9@example.com"},
        {"first_name": "Павел", "last_name": "Морозов", "contact_info": "email10@example.com"},
    ]

    for master_data in masters_data:
        master = Master.objects.create(
            first_name=master_data["first_name"],
            last_name=master_data["last_name"],
            contact_info=master_data["contact_info"]
        )
        # Присваиваем случайные 3 услуги мастеру
        master.services.set(random.sample(services, 3))

def main():
    services = create_services()
    create_masters(services)
    print("Заполнено")

if __name__ == "__main__":
    main()
