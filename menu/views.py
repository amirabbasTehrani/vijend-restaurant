from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import Category, MenuItem

# Create your views here.

class HomePageView(ListView):
    model = Category
    template_name = 'menu/index.html'
    context_object_name = 'Categories'
    
    def get_queryset(self):
        return Category.objects.filter(parent__isnull=True)
    
