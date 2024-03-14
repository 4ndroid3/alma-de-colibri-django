from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    """Represents a product in the store."""

    name = models.CharField(max_length=70)
    description = models.TextField(max_length=200, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    category = models.ManyToManyField("Category", related_name="products")
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="created_products", null=True
    )
    updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="updated_products", null=True, blank=True
    )

    def __str__(self):
        return self.name

    def get_gain(self) -> float:
        """Calculate the gain of the product."""
        return self.price - self.cost


class Category(models.Model):
    """Represents a category for products in the store."""

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="created_category", null=True
    )
    updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="updated_category", null=True, blank=True
    )

    def __str__(self):
        return self.name
