from django.urls import path

from products.views import CategoryCreateView, CategoryViewList, ProductCreateView, ProductViewList

urlpatterns = [
    path("", ProductViewList.as_view(), name="product_list"),
    path("new/", ProductCreateView.as_view(), name="product_create"),
    path("categories/", CategoryViewList.as_view(), name="category_list"),
    path("categories/new", CategoryCreateView.as_view(), name="category_create"),
]
