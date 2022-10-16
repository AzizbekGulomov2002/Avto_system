from django.urls import path
from django.contrib.auth.views import LoginView

from . import views
from .forms import UserLoginForm

app_name = 'account'

urlpatterns = [
    path('register/', views.account_register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
