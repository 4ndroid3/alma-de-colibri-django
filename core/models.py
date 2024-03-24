from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    related_discount = models.ForeignKey(
        "products.Discount", on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self) -> str:
        return self.username


class Address(models.Model):
    street_address = models.CharField(max_length=100)
    related_city = models.ForeignKey("City", on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    related_user = models.ForeignKey("User", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.street_address} - {self.related_city.name}"


class City(models.Model):
    name = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    description = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
