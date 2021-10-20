from django.urls import include, path

from rest_framework import routers

from .views import ItemsViewSet, BoxViewSet

router = routers.DefaultRouter()
router.register(r'items', ItemsViewSet)
router.register(r'boxes', BoxViewSet)

urlpatterns = [
   path('', include(router.urls)),
]