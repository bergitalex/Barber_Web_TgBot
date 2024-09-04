document.getElementById('master').addEventListener('change', function() {
    const masterId = this.value;

    fetch(`/services/?master_id=${masterId}`)
        .then(response => response.json())
        .then(data => {
            const serviceSelect = document.getElementById('service');
            serviceSelect.innerHTML = '';  // Очищаем текущие опции

            if (data.services.length > 0) {
                data.services.forEach(service => {
                    const option = document.createElement('option');
                    option.value = service.id;
                    option.textContent = `${service.name} - ${service.price} руб.`;
                    serviceSelect.appendChild(option);
                });
            } else {
                const option = document.createElement('option');
                option.textContent = 'Нет доступных услуг';
                serviceSelect.appendChild(option);
            }
        })
        .catch(error => console.error('Ошибка:', error));
});