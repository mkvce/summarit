from django.urls import path
from url_shortener import views

app_name = 'url_shortener'
urlpatterns = [
    path('', views.home, name='home'),
    path('u/<slug:code>/', views.short_url, name='short_url'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add_url/', views.add_url, name='add_url'),
]
