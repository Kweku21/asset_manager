from django.conf import settings
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = settings.SITE_HEADER
admin.site.site_title = settings.SITE_HEADER

urlpatterns = [
    path('', include('source.apps.users.urls')),
    path('admin/', admin.site.urls),
]
