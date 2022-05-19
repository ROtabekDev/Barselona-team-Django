

from django.conf.urls.static import static
from coolsite import settings
from django.contrib import admin
from django.urls import path, include

from players.views import pageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("players.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound
