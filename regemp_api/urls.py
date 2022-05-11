from django.urls import path, include
from regemp_api import views

urlpatterns = [
    path('departamento/<id>/', views.DepartamentoDetail.as_view()),
    path('departamento/', views.DepartamentoList.as_view()),
    path('empleado/<id>', views.EmpleadoDetail.as_view()),
    path('empleado/', views.EmpleadoList.as_view()),
    path('perfil/<id>', views.PerfilDetail.as_view()),
    path('perfil/', views.PerfilList.as_view()),
    path('usuario/<id>', views.UsuarioDetail.as_view()),
    path('usuario/', views.UsuarioList.as_view()),

]
