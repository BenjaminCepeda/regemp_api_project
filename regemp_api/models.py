from djongo import models


class Departamento(models.Model):
    descripcion = models.CharField(max_length=50)
    estado = models.SmallIntegerField()

class Perfil(models.Model):
    descripcion = models.CharField(max_length=20)
    esAdministrador = models.SmallIntegerField()
    estado = models.SmallIntegerField()

class Usuario(models.Model):
    nombreUsuario=models.CharField(max_length=20)
    clave = models.CharField(max_length=15)
    perfil = models.ForeignKey(Perfil, on_delete=models.SET_NULL, null=True, related_name='perfil')
    estado = models.SmallIntegerField()

class Empleado(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    celular = models.CharField(max_length=13)
    email = models.CharField(max_length=50)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True,
                                related_name='usuario')
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL,
                                     null=True, related_name='departamento')
    estado = models.SmallIntegerField()
