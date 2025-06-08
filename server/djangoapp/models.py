# Uncomment the following imports before adding the Model code

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"`{self.name}`, `{self.description}`"


class CarModel(models.Model):
    MODEL_TYPES = [
        ("SEDAN", "Sedan"),
        ("SUV", "SUV"),
        ("WAGON", "Wagon"),
    ]

    name = models.CharField(max_length=100)
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealerId = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
    type = models.CharField(
        max_length=10,
        default="SUV",
        choices=MODEL_TYPES
    )
    year = models.IntegerField(
        default=2023,
        validators=[MaxValueValidator(2023), MinValueValidator(2015)]
    )

    def __str__(self):
        return (
            f"`{self.name}`, `{self.car_make}`, `{self.dealerId}`, "
            f"`{self.type}`, `{self.year}`"
        )
