from django.urls import path

from . import views

urlpatterns = [
    path('menu-details/',views.MenuListView.as_view(),name='menu-details'),
    path('menu-registration/',views.MenuCreateView.as_view(),name='menu-reg'),
]