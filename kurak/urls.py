
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from kurakshopprojekt import views  # сенин views.py файлы

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Бул башкы бетти кошту
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kurakshopprojekt.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)