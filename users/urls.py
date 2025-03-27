from django.urls import path
from .views import register, login_view, home
from . import views 

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
]
