# Web/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Visit
from .tasks import run_async_function, send_telegram_message

@receiver(post_save, sender=Visit)
def notify_telegram(sender, instance, created, **kwargs):
    if created:
        run_async_function(send_telegram_message,
            instance.client_name,
            instance.phone,
            instance.master.first_name,  # Передаем имя мастера
            instance.service.name,       # Передаем название услуги
            instance.appointment_date
        )
        print("Запись отправлена")
