from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from app import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/biblioteca/', permanent=False)),
    path('biblioteca/', include(urls))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Adicionar Isto
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Adicionar Isto 