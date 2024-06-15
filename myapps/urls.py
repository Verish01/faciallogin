from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.query_view, name='query_view'),  # Set query_view as the main page
    path('inventory/', views.inventory_list, name='inventory_list'),  # Moved inventory_list to a different URL
    path('clear_history/', views.clear_history, name='clear_history'),
    path('download_history_xml/', views.download_history_xml, name='download_history_xml'),
    path('upload-csv/', views.upload_csv, name='upload_csv'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
