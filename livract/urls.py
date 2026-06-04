from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('accounts.urls')),
    path('books/', include('books.urls')),
    path('exchanges/', include('exchanges.urls')),
    path('events/', include('events.urls')),
    path('notifications/', include('notifications.urls')),
    path('moderation/', include('moderation.urls')),
    path('pro/', include('professionals.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
