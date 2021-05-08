from django.urls import path
from url_shortener import views

app_name = 'url_shortener'
urlpatterns = [
    path('', views.home, name='home'),
    path('u/<slug:code>/', views.short_url, name='short_url'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='log'),
]
