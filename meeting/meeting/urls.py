from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from django.conf.urls.static import static
from django.conf import settings
from landing.views import LandingPage

api = NinjaAPI()

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
    path("", LandingPage, name= "landingpage")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
