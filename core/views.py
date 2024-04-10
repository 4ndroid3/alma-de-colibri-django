from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from products.models import Product


def index(request):
    return render(request, 'core/index.html')

def emergency_products_reset(request):
    try:
        Product.objects.all().delete()
        return HttpResponse("<h1>Borrado exitoso</h1>")
    except Exception as e:
        print(e)
        return HttpResponse("<h1>Hubo un error</h1>")
