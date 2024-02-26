from django.urls import path
from . import views
from django.conf import settings

app_name = 'blog'  # Define the app namespace


urlpatterns = [
    path('home/', views.home, name='home'),
    path('create_ticket/', views.create_ticket, name="create_ticket"),
]

