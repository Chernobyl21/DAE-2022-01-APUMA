from django.urls import path

from . import views

app_name = 'volumenc'

urlpatterns = [
    path('',views.index, name='index'),
    path('formulario_cilindro', views.formulario_cilindro, name='formulario_cilindro'),
    path('fcilindro_respuesta', views.fcilindro_respuesta, name='fcilindro_respuesta'),
]