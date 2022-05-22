from rest_framework import serializers
from regemp_api.models import *


class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = "__all__"


class DepartamentoSerializer(serializers.ModelSerializer):
    estado = EstadoSerializer(many=False, read_only=True)
    idEstado = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Estado.objects.all(), source='estado')

    class Meta:
        model = Departamento
        fields = ('id', 'descripcion', 'idEstado', 'estado')


class PerfilSerializer(serializers.ModelSerializer):
    estado = EstadoSerializer(many=False, read_only=True)
    idEstado = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Estado.objects.all(), source='estado')

    class Meta:
        model = Perfil
        fields = ('id', 'descripcion', 'esAdministrador', 'idEstado', 'estado')


class UsuarioSerializer(serializers.ModelSerializer):
    perfil= PerfilSerializer(many=False, read_only=True)
    idPerfil = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Perfil.objects.all(), source='perfil')
    estado = EstadoSerializer(many=False, read_only=True)
    idEstado = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Estado.objects.all(), source='estado')

    class Meta:
        model = Usuario
        fields = ('id', 'nombreUsuario', 'clave', 'idPerfil', 'idEstado',
                  'perfil', 'estado')


class EmpleadoSerializer(serializers.ModelSerializer):
    usuario= UsuarioSerializer(many=False, read_only=True)
    idUsuario = serializers.PrimaryKeyRelatedField(write_only=True,
                    queryset=Usuario.objects.all(), source='usuario')
    departamento= DepartamentoSerializer(many=False, read_only=True)
    idDepartamento = serializers.PrimaryKeyRelatedField(write_only=True,
                    queryset=Departamento.objects.all(), source='departamento')
    estado = EstadoSerializer(many=False, read_only=True)
    idEstado = serializers.PrimaryKeyRelatedField(write_only=True,
                            queryset=Estado.objects.all(), source='estado')

    class Meta:
        model = Empleado
        fields = ('id', 'nombres', 'apellidos', 'direccion', 'celular',
                  'email', 'idUsuario', 'usuario', 'idDepartamento',
                  'departamento', 'foto', 'idEstado', 'estado')
