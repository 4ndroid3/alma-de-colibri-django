from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('/products-reset', views.emergency_products_reset, name='products-reset')
]