from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("save", views.save, name="save"),
    path("pessoa/<int:pessoa_id>", views.pessoa_detail, name="pessoa_detail"),
    path("delete/<int:pessoa_id>", views.pessoa_delete, name="pessoa_delete"),
    path("update/<int:pessoa_id>", views.pessoa_update, name="pessoa_update"),
    path("ping", views.ping, name="ping"),
    path("exception", views.exceptionExample, name="exception"),
]
