from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("<int:attributes_id>/", views.detail, name = "detail"),
    path("<int:attributes_id>/upgrade", views.upgrade, name = "upgrade"),
]

