from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_dir=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL_URL, document_dir=settings.MEDIA_ROOT_ROOT)



