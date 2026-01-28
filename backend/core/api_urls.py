from django.urls import path
from .api_views import health_check, profile

urlpatterns = [
    path("health/", health_check),
    path("profile/", profile),
]
