from django.db import models



from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Car(models.Model):
    ENGINE_TYPES = [
        ('petrol', 'Petrol'),
        ('diesel', 'Diesel'),
        ('electric', 'Electric'),
        ('hybrid', 'Hybrid'),
    ]

    TRANSMISSION_TYPES = [
        ('manual', 'Manual'),
        ('automatic', 'Automatic'),
    ]

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')
    name = models.CharField(max_length=50)
    engine_type = models.CharField(max_length=20, choices=ENGINE_TYPES)
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_TYPES)
    color = models.CharField(max_length=30)
    max_speed = models.IntegerField()
    mileage = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='photo/', blank=True, null=True)

    def __str__(self):
        return f"{self.brand.name} {self.name}"