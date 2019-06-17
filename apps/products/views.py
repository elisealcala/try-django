import json
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from react.views import ReactView

# Create your views here.
class ProductsView(ReactView):
    template_name = "products.html"

    def get_context_data(self, **kwargs):
        context = super(ProductsView, self).get_context_data(**kwargs)
        # data = JsonResponse(Product.objects.all(), safe=False)
        data={"('Hello',)": 6, "('Hi',)": 5}
        self.set_initial_state('products', json.dumps(data))
        print(json.dumps(data))
        return context

