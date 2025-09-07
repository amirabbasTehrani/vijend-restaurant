from django.views.generic import TemplateView, DetailView
from django.shortcuts import get_object_or_404
from .models import Category, MenuItem


class HomePageView(TemplateView):
    template_name = 'menu/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # only children categories (have a parent)
        context['sub_categories'] = (
            Category.objects.filter(parent__isnull=False)
            .order_by(F('priority').desc(nulls_last=True), 'title')
        )
        return context



class MenuItemListView(DetailView):
    model = Category
    template_name = 'menu/items.html'
    context_object_name = 'category'
    slug_url_kwarg = 'slug'

    def get_object(self):
        parent_slug = self.kwargs['parent_slug']
        sub_slug = self.kwargs['slug']
        return get_object_or_404(Category, slug=sub_slug, parent__slug=parent_slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = self.object.items.filter(is_available=True).order_by('-priority')
        return context
