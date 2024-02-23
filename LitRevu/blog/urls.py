from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('create_ticket/', views.create_ticket, name="create_ticket"),
    path("create_ticket/", views.create_ticket, name="create-ticket"),
]
