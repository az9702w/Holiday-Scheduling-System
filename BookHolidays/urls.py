from django.urls import path
from .import views


urlpatterns = [
    path('booking/', views.different_dates, name= 'bookholidays'), 
    path('accounts/', views.accounts, name= 'accounts'),
]