from django.urls import path
from .views import HomePageView, MenuItemListView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('menu/<slug:parent_slug>/<slug:slug>/', MenuItemListView.as_view(), name='menuitem-list'),
    ]