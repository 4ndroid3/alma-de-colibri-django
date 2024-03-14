from django.views.generic import ListView
from django.views.generic.edit import CreateView

from products.forms import CategoryForm, ProductForm
from products.models import Category, Product
from project.custom_mixins import RegisterUserOnForm


class ProductViewList(ListView):
    model = Product
    context_object_name = "products"
    ordering = ["-created_at"]
    paginate_by = 10


class ProductCreateView(RegisterUserOnForm, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "products/product_form.html"
    success_url = "/products"


class CategoryViewList(ListView):
    model = Category
    context_object_name = "categories"
    ordering = ["-created_at"]
    paginate_by = 10
    template_name = "products/category_list.html"


class CategoryCreateView(RegisterUserOnForm, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "products/category_form.html"
    success_url = "/products/categories"
