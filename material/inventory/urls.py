from django.urls import path, include
from .views import ItemListView, UserItemListView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView, BoxListView, BoxDetailView, PisoItemListView
from . import views

urlpatterns = [
    path('home/', ItemListView.as_view(), name='inventory-home'),
    path('home/box-list/', BoxListView.as_view(), name='box-list'),
    path('user/<str:username>/', UserItemListView.as_view(), name='user-items'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('box/<str:piso>/<int:pk>', BoxDetailView.as_view(), name='box-detail'),
    path('item/new/', ItemCreateView.as_view(), name='item-create'),
    path('item/<int:pk>/update/', ItemUpdateView.as_view(), name='item-update'),
    path('item/<int:pk>/delete/', ItemDeleteView.as_view(), name='item-delete'),
    path('info/', views.info, name='inventory-info'),
    path('pisos/', views.pisos, name='pisos-list'),
    path('piso/<str:piso>/', PisoItemListView.as_view(), name='piso-items'),

]