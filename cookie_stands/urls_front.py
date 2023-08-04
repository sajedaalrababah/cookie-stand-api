from django.urls import path
from .views_front import (
    cookie_standCreateView,
    cookie_standDeleteView,
    cookie_standDetailView,
    cookie_standListView,
    cookie_standUpdateView,
)

urlpatterns = [
    path("", cookie_standListView.as_view(), name="cookie_stand_list"),
    path("<int:pk>/", cookie_standDetailView.as_view(), name="cookie_stand_detail"),
    path("create/", cookie_standCreateView.as_view(), name="cookie_stand_create"),
    path("<int:pk>/update/", cookie_standUpdateView.as_view(), name="cookie_stand_update"),
    path("<int:pk>/delete/", cookie_standDeleteView.as_view(), name="cookie_stand_delete"),
]
