from django.urls import path
from . import views
urlpatterns = [
    path('users/',views.user_index, name = "user.index"),
    path('',views.landing, name= 'landing'),
    path('users/login/', views.user_login, name = "user.login"),
    path('users/create/', views.user_register, name ="user.create"),
    path('users/logout', views.user_logout, name = "user.logout"),
]