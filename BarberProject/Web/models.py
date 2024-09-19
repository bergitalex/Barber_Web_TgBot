from django.db import models

class Master(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact_info = models.TextField()
    photo = models.ImageField(upload_to='masters_img', blank=True)
    services = models.ManyToManyField('Service')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Service(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f'{self.name} ({self.price} руб.)'

class Visit(models.Model):
    client_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
