from django.urls import path
from . import views

urlpatterns = [
    path('mi-modelo/', views.mi_modelo_lista, name='mi_modelo_lista'),
    path('segundo-modelo/', views.segundo_modelo_lista, name='segundo_modelo_lista'),
    path('tercer-modelo/', views.tercer_modelo_lista, name='tercer_modelo_lista'),
]
