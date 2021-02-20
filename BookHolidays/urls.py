from django.urls import path
from .import views


urlpatterns = [
    path('booking/', views.bookholidays, name= 'bookholidays'),
    path('', views.accounts, name= 'accounts')
  
]