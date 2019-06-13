from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from react.views import ReactView

# Create your views here.
class ProductsView(ReactView):
    template_name = "products.html"
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProductsView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        obj = Product.objects.get(id=1)
        context['product'] = obj
        return context

# def products_view(request, *args, **kwargs):
#     obj = Product.objects.get(id=1)
#     context = {
#       'title': obj.title,
#       'description': obj.description
#     }
#     return render(request, "products.html", context)
