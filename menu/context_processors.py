from .models import Category

def parent_categories(request):
    return {
        'parent_categories_nav': Category.objects.filter(parent__isnull=True).prefetch_related('children')
    }
