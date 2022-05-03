from django.urls import path
from regemp_api import views

urlpatterns = [
    path('departamento/', views.DepartamentoList.as_view()),
    path('empleado/', views.EmpleadoList.as_view()),
]