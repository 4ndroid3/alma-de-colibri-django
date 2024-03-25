from django.urls import include, path

from api.core import urls as core_urls
from api.products import urls as products_urls
from api.sales import urls as sales_urls

urlpatterns = [
    path("products/", include(products_urls), name="products"),
    path("sales/", include(sales_urls), name="sales"),
    path("core/", include(core_urls), name="core"),
]
