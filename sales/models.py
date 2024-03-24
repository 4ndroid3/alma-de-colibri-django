from django.db import models


class Sale(models.Model):
    PAID = "paid"
    PENDING = "pending"
    SHIPPED = "shipped"
    DELIVERED = "delivered"

    SALE_STATUS = [
        (PENDING, "Pending"),
        (PAID, "Paid"),
        (SHIPPED, "Shipped"),
        (DELIVERED, "Delivered"),
    ]

    status = models.CharField(max_length=20, choices=SALE_STATUS, default=PENDING)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    related_user = models.ForeignKey("core.User", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.status}"


class SaleDetail(models.Model):
    related_sale = models.ForeignKey("Sale", on_delete=models.CASCADE, related_name="details")
    related_product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.sale}"


class Cart(models.Model):
    """Its a cart for a user."""

    related_user = models.ForeignKey("core.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.related_user.username} cart"


class CartDetail(models.Model):
    related_cart = models.ForeignKey("Cart", on_delete=models.CASCADE, related_name="details")
    related_product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.related_cart}"
