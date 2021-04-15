from django.contrib import admin
from django.urls import path,include

####static debug mode###################################################
from django.conf import settings
from django.conf.urls.static import static
from . import views

########################################################################
app_name ="gold"
urlpatterns = [
path('login', views.loginpage,name="login"),
]


if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
