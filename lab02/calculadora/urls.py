from django.urls import path

from . import views

app_name = 'calculadora'

urlpatterns = [
    path('',views.index, name='index'),
    path('enviar', views.enviar, name='enviar'),

    path('formulario_tarea', views.formulario_tarea, name='formulario_tarea'),
    path('respuesta', views.respuesta, name='respuesta'),
]
