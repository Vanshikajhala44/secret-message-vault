from django.urls import path
from . import views

urlpatterns = [
    path("", views.create_message, name="create"),
      path("success/<uuid:secret_id>/", views.success, name="success"),
      path("message/<uuid:secret_id>/", views.view_message, name="view"),

]
