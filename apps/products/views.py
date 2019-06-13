from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
def products_view(request, *args, **kwargs):
    obj = Product.objects.get(id=1)
    context = {
      'title': obj.title,
      'description': obj.description
    }
    return render(request, "products.html", context)
