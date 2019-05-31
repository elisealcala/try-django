from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def products_view(request, *args, **kwargs):
    return render(request, "products.html", {})
