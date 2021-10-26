from django.urls import include, path

from rest_framework import routers

from .views import ItemsViewSet, BoxViewSet

router = routers.DefaultRouter()
router.register(r'items', ItemsViewSet, basename='items')
router.register(r'boxes', BoxViewSet, basename='boxes')

urlpatterns = [
   path('', include(router.urls)),
]
