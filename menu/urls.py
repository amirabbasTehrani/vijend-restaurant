from django.urls import path
from .views import HomePageView, MenuItemListView
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('menu/<slug:parent_slug>/<slug:slug>/', MenuItemListView.as_view(), name='menuitem-list'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
