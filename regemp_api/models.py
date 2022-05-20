from djongo import models

class Estado(models.Model):
    descripcion = models.CharField(max_length=50)
    color = models.CharField(max_length=7)

class Departamento(models.Model):
    descripcion = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.RESTRICT, null=False,
                                 related_name='estadoDepartamento')


class Perfil(models.Model):
    descripcion = models.CharField(max_length=20)
    esAdministrador = models.SmallIntegerField()
    estado = models.ForeignKey(Estado, on_delete=models.RESTRICT, null=False,
                                 related_name='estadoPerfil')


class Usuario(models.Model):
    nombreUsuario=models.CharField(max_length=20)
    clave = models.CharField(max_length=15)
    perfil = models.ForeignKey(Perfil, on_delete=models.RESTRICT, null=False,
                                 related_name='perfil')
    estado = models.ForeignKey(Estado, on_delete=models.RESTRICT, null=False,
                                 related_name='estadoUsuario')

class Empleado(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    celular = models.CharField(max_length=13)
    email = models.CharField(max_length=50)
    usuario = models.ForeignKey(Usuario, on_delete=models.RESTRICT,
                                  null=False, related_name='usuario')
    departamento = models.ForeignKey(Departamento, on_delete=models.RESTRICT,
                                     null=False, related_name='departamento')
    foto = models.ImageField()
    estado = models.ForeignKey(Estado, on_delete=models.RESTRICT, null=False,
                                 related_name='estadoEmpleado')

