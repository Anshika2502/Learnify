from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login , name='login'),
    path('register/', views.register , name='register'),
    path('logout/', views.logout , name='logout'),
    path('my_profile/', views.my_profile , name='my_profile'),
]