# Web/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Reservation
from .tasks import run_async_function, send_telegram_message

@receiver(post_save, sender=Reservation)
def notify_telegram(sender, instance, created, **kwargs):
    if created:
        run_async_function(send_telegram_message,
            instance.name,
            instance.phone,
            instance.master.first_name,  # Передаем имя мастера
            instance.service.name       # Передаем название услуги
        )
        print("Запись отправлена")
