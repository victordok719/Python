from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('hello/<str:username>',views.hello),
    #path('usuarios/', views.usuarios),
    #path('listas/', views.listas)
]