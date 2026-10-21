from django.urls import path
from . import views

app_name = "characters"
urlpatterns = [
    path("", views.index, name = "index"),
    path("<int:character_id>/", views.detail, name = "detail"),
    path("<int:character_id>/upgrade", views.upgrade, name = "upgrade"),
    path("<int:character_id>/downgrade", views.downgrade, name = "downgrade"),
    path("create/", views.create, name = "create")
]

