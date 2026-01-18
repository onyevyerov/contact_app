from django.urls import path, include
from rest_framework import routers

from api.views import ContactViewSet

router = routers.DefaultRouter()
router.register("contacts", ContactViewSet, basename="contact-api")

urlpatterns = [
    path("api/", include(router.urls)),
]

app_name = "api"