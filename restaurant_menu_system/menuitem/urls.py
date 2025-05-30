from django.urls import path

from . import views

urlpatterns = [
    path('menuitem-details/',views.MenuitemListView.as_view(),name='menuitem-details'),
    path('menuitem-registration/',views.MenuitemCreateView.as_view(),name='menuitem-reg'),
    path('menuitem-update/<str:uuid>/',views.MenupriceUpdateView.as_view(),name='menuitem-update'),
]