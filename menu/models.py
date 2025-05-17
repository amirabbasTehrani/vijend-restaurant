from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=155, unique=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='menu_items/', blank=True, null=True)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='children'
    )
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("category-detail", kwargs={"pk": self.pk})

class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    title = models.CharField(max_length=155)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=0, blank=True, null=True)
    image = models.ImageField(upload_to='menu_items/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['category', 'title']

    def __str__(self):
        return self.title