
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from kurakshopprojekt import views  # сенин views.py файлы
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kurakshopprojekt.urls')),  # подключение URL приложения
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # allauth жолдору
]




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kurakshopprojekt.urls')),  # биздин фронттын urls
]

# Media файлын локал көрсөтүү
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns = [
    path('', views.home, name='home'),
    path('camera/', views.camera_view, name='camera'),
]

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