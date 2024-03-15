from django.contrib import admin

from products.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created_at", "updated_at", "created_by", "updated_by")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "price",
        "cost",
        "get_gain",
        "created_at",
        "updated_at",
        "created_by",
        "updated_by",
    )
