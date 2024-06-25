from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('registration', views.registration, name='registration'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('home', views.home, name='home')

]
