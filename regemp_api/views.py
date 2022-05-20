from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from regemp_api.serializers import *
from regemp_api.models import *
from django.db.models.query_utils import Q

class EmpleadoList(APIView):
    def get(self, request):
        empleados = Empleado.objects.all()
        email = request.GET.get('email', None)
        pwd = request.GET.get('pwd', None)
        if email is not None:
            empleados = empleados.filter(Q(email__iexact=email) |
                Q(idUsuario__nombreUsuario=email), idUsuario__clave__exact=pwd)
        serializer = EmpleadoSerializer(empleados, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmpleadoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmpleadoDetail(APIView):
    def get(self, requestid, id):
        try:
            empleado = Empleado.objects.get(id=id)
            if empleado:
                serializer = EmpleadoSerializer(empleado)
                return Response(serializer.data)
        except Exception as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status.HTTP_200_OK)

    def put(self, request, id):
        try:
            empleado = Empleado.objects.get(id=id)
            if empleado:
                serializer = EmpleadoSerializer(empleado, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            empleado = Empleado.objects.get(pk=id)
            empleado.delete()
            return Response(status.HTTP_200_OK)
        except Exception as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class PerfilDetail(APIView):

    def get(self, requestid, id):
        try:
            perfil = Perfil.objects.get(id=id)
            if perfil:
                serializer = PerfilSerializer(perfil)
                return Response(serializer.data)
        except Exception as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status.HTTP_200_OK)

    def put(self, request, id):
        try:
            perfil = Perfil.objects.get(pk=id)
            if perfil:
                serializer = PerfilSerializer(perfil, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            perfil = Perfil.objects.get(pk=id)
            perfil.delete()
            return Response(status.HTTP_200_OK)
        except Exception as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class PerfilList(APIView):
    def get(self, requestid):
        perfiles = Perfil.objects.all()

        serializer = PerfilSerializer(perfiles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PerfilSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepartamentoDetail(APIView):

    def get(self, requestid, id):

        try:
            departamento = Departamento.objects.get(pk=id)
            if departamento:
                serializer = DepartamentoSerializer(departamento)
                return Response(serializer.data)
        except Exception as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status.HTTP_200_OK)

    def put(self, request, id):
        try:
            departamento = Departamento.objects.get(pk=id)
            if departamento:
                serializer = DepartamentoSerializer(departamento, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            departamento = Departamento.objects.get(pk=id)
            departamento.delete()
            return Response(status.HTTP_200_OK)
        except Exception as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class DepartamentoList(APIView):
    def get(self, requestid):
        departamentos = Departamento.objects.all()

        serializer = DepartamentoSerializer(departamentos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DepartamentoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuarioDetail(APIView):

    def get(self, requestid, id):

        try:
            usuario = Usuario.objects.get(pk=id)
            if usuario:
                serializer = UsuarioSerializer(usuario)
                return Response(serializer.data)
        except Exception as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status.HTTP_200_OK)

    def put(self, request, id):
        try:
            usuario = Usuario.objects.get(pk=id)
            if usuario:
                serializer = UsuarioSerializer(usuario, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            usuario = Usuario.objects.get(pk=id)
            usuario.delete()
            return Response(status.HTTP_200_OK)
        except Exception as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UsuarioList(APIView):
    def get(self, requestid):
        usuarios = Usuario.objects.all()

        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EstadoDetail(APIView):

    def get(self, requestid, id):

        try:
            estado = Estado.objects.get(pk=id)
            if estado:
                serializer = DepartamentoSerializer(estado)
                return Response(serializer.data)
        except Exception as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status.HTTP_200_OK)

    def put(self, request, id):
        try:
            estado = Estado.objects.get(pk=id)
            if estado:
                serializer = EstadoSerializer(estado, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            estado = Departamento.objects.get(pk=id)
            estado.delete()
            return Response(status.HTTP_200_OK)
        except Exception as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class EstadoList(APIView):
    def get(self, requestid):
        estados = Estado.objects.all()

        serializer = EstadoSerializer(estados, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EstadoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
