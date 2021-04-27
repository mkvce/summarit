from django.urls import path
from url_shortener import views

app_name = 'url_shortener'
urlpatterns = [
    path('u/<slug:code>/', views.short_url, name='short_url'),
]
