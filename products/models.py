from django.db import models


class Product(models.Model):
    """Represents a product in the store."""

    name = models.CharField(max_length=70)
    description = models.TextField(max_length=200, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    related_categories = models.ManyToManyField("Category", related_name="products")
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    stock = models.IntegerField(default=0)
    last_restocked_at = models.DateField(null=True, blank=True)
    expiration_days = models.IntegerField(null=True, blank=True)
    related_discount = models.ForeignKey(
        "Discount", on_delete=models.SET_NULL, null=True, blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        "core.User", on_delete=models.SET_NULL, related_name="created_products", null=True
    )
    updated_by = models.ForeignKey(
        "core.User",
        on_delete=models.SET_NULL,
        related_name="updated_products",
        null=True,
        blank=True,
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
    related_discount = models.ForeignKey(
        "Discount", on_delete=models.SET_NULL, null=True, blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        "core.User", on_delete=models.SET_NULL, related_name="created_category", null=True
    )
    updated_by = models.ForeignKey(
        "core.User",
        on_delete=models.SET_NULL,
        related_name="updated_category",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Discount(models.Model):
    """Represents a discount for many elements in the store."""

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, blank=True, null=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        "core.User", on_delete=models.SET_NULL, related_name="created_discount", null=True
    )
    updated_by = models.ForeignKey(
        "core.User",
        on_delete=models.SET_NULL,
        related_name="updated_discount",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
