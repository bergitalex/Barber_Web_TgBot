from django.db import models

class Master(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact_info = models.TextField()
    photo = models.ImageField(upload_to='masters_img', blank=True)
    services = models.ManyToManyField('Service')

class Service(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2, max_digits=10)

class Reservation(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)