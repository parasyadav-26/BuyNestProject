from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name="index" ),
    path('home/', views.home_view, name="home_view"),
    path('register/', views.register_view, name="register"),
    path('login/',views.login_view, name="login")
]