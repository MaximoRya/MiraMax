from django.urls import path
from . import views

urlpatterns = [
    # Главная страница с описанием
    path('', views.index),
    # Краткое описание процедур салона
    path('salon/', views.salon_info),
    # Подробное описание и запись на процедуру
    path('salon/<pk>/', views.salon_turnos),
] 