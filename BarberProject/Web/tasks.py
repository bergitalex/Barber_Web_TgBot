import telegram
from django.conf import settings
import logging
import asyncio

# Настройка логгера для отслеживания ошибок
logger = logging.getLogger(__name__)


async def send_telegram_message(name, phone, master_name, service_name):
    try:
        # Создаем экземпляр бота с токеном
        bot = telegram.Bot(token=settings.TELEGRAM_BOT_TOKEN)

        # Формируем сообщение
        message = (
            f'Новая заявка:\n'
            f'Имя: {name}\n'
            f'Телефон: {phone}\n'
            f'Мастер: {master_name}\n'
            f'Услуга: {service_name}'
        )

        # Отправляем сообщение в указанный чат с использованием await
        await bot.send_message(chat_id=settings.ADMIN_CHAT_ID, text=message)

        logger.info(f"Сообщение успешно отправлено: {message}")
        print("Сообщение успешно отправлено")
    except Exception as e:
        logger.error(f"Ошибка при отправке сообщения в Telegram: {e}")
        print(f"Ошибка: {e}")


# Функция для запуска асинхронного кода
def run_async_function(func, *args):
    try:
        # Получаем текущий цикл событий
        loop = asyncio.get_event_loop()
    except RuntimeError:
        # Если цикл не запущен, создаем новый
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    # Если цикл уже запущен, используем его, иначе запускаем новую задачу
    if loop.is_running():
        # Запускаем задачу в уже запущенном цикле
        task = loop.create_task(func(*args))
    else:
        # Запускаем цикл событий
        loop.run_until_complete(func(*args))


