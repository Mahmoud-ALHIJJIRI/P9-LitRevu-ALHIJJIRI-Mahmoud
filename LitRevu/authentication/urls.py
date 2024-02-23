from django.contrib.auth.views import LoginView
from django.urls import path
from . import views


urlpatterns = [
    path('login/', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True),
         name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup_page, name='signup'),
]
