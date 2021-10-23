from django.urls import path, include
from .views import ItemListView, UserItemListView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView, BoxListView, BoxDetailView, PisoItemListView, BoxCreateView, BoxUpdateView, BoxDeleteView, ApiItems
from . import views

urlpatterns = [
    path('home/', ItemListView.as_view(), name='inventory-home'),
    path('item/new/', ItemCreateView.as_view(), name='item-create'),
    path('item/<int:pk>/update/', ItemUpdateView.as_view(), name='item-update'),
    path('item/<int:pk>/delete/', ItemDeleteView.as_view(), name='item-delete'),
    path('user/<str:username>/', UserItemListView.as_view(), name='user-items'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('info/', views.info, name='inventory-info'),
    path('pisos/', views.pisos, name='pisos-list'),
    path('piso/<str:piso>/', PisoItemListView.as_view(), name='piso-items'),

    path('box/<int:pk>/delete/', BoxDeleteView.as_view(), name='box-delete'),#all these are fine, but they need to recognise duplicate boxes
    path('box/<int:pk>/update/', BoxUpdateView.as_view(), name='box-update'),
    path('box/new/', BoxCreateView.as_view(), name='box-create'),

    path('box/<str:piso>/<int:number>/', BoxDetailView.as_view(), name='box-detail'),
    path('home/box-list/', BoxListView.as_view(), name='box-list-view'),
    
    #path('api/items/', ApiItems.as_view(), name='api-items'),#this is just a test, can be removed
]