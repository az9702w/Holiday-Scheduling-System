from django.urls import path
from . import views


urlpatterns = [
    path('OtherTypes/', views.othertypes, name= 'OtherTypes'),
    path('MaternityLeaves/', views.maternity, name= 'MaternityLeaves'),
     path('PaternityLeaves/', views.paternity, name= 'PaternityLeaves'),
    path('BookHolidays/', views.bookholidays, name= 'BookHolidays'),
    path('accounts/', views.accounts, name= 'Accounts'),
    path('PreviousHistory/', views.history, name= 'History')
]