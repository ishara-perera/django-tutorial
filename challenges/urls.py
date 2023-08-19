from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:month>', views.monthly_challenge_by_number, name='month_number'),
    path('<str:month>', views.monthly_challenge, name='month'),
]