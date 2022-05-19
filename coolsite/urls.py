

from django.contrib import admin
from django.urls import path, include

from players.views import pageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("players.urls")),
]

handler404 = pageNotFound
