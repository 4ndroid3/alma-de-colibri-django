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
    list_filter = ("category",)
    search_fields = ("name", "description")
    date_hierarchy = "created_at"
    ordering = ("price",)
    filter_horizontal = ("category",)
    readonly_fields = ("get_gain",)
    fieldsets = (
        (
            "Product",
            {
                "fields": (
                    "name",
                    "description",
                    "price",
                    "cost",
                    "category",
                    "image",
                )
            },
        ),
        (
            "Audit",
            {
                "fields": (
                    "created_by",
                    "updated_by",
                ),
                "classes": ("collapse",),
            },
        ),
    )
    raw_id_fields = ("created_by", "updated_by")
    autocomplete_fields = ("created_by", "updated_by")
    # radio_fields = {"category": admin.HORIZONTAL}
    prepopulated_fields = {"description": ("name",)}
    save_as = True
    save_on_top = True
    actions_on_top = True
    actions_on_bottom = False
    list_per_page = 10
    list_max_show_all = 100
    list_editable = ("price", "cost")
