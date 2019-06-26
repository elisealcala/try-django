from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

# Create your views here.
from .models import Article


class ArticleListView(ListView):
    queryset = Article.objects.all()
