

from django.contrib import admin
from django.urls import path,include

####static debug mode###################################################
from django.conf import settings
from django.conf.urls.static import static

########################################################################

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gold.urls')),
]


if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
