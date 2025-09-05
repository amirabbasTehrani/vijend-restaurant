from django.views.generic import TemplateView, DetailView
from django.shortcuts import get_object_or_404
from django.db.models import Prefetch, F
from .models import Category, MenuItem

class HomePageView(TemplateView):
    template_name = 'menu/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Prefetch children ordered by priority descending, NULLs last, then title
        children_qs = Category.objects.order_by(F('priority').desc(nulls_last=True), 'title')

        # Parent categories ordered by priority descending, NULLs last, then title
        context['parent_categories'] = (
            Category.objects.filter(parent__isnull=True)
            .prefetch_related(Prefetch('children', queryset=children_qs))
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
        # Items ordered by priority descending, NULLs last, then title
        context['items'] = self.object.items.filter(is_available=True).order_by(
            F('priority').desc(nulls_last=True), 'title'
        )
        return context
