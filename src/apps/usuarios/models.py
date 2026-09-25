from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class CustomUserManager(UserManager):
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('rol', CustomUser.Roles.ADMIN)
        return super().create_superuser(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = 'ADMIN', 'Administrador'
        MESERO = 'MESERO', 'Mesero'
        CAJERO = 'CAJERO', 'Cajero'
        COCINA = 'COCINA', 'Cocina'

    rol = models.CharField(
        max_length=10,
        choices=Roles.choices,
        default=Roles.MESERO,
        verbose_name="Rol del Usuario"
    )

    def __str__(self):
        return f"{self.username} ({self.get_rol_display()})"

class RegistroAsistencia(models.Model):
    usuario = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='asistencias'
    )
    fecha = models.DateField(auto_now_add=True)
    hora_entrada = models.DateTimeField(auto_now_add=True)
    hora_salida = models.DateTimeField(null=True, blank=True)
    horas_trabajadas = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = "Regitro de Asistencia"
        verbose_name_plural = "Registros de Asistencia"

    def __str__(self):
        return f"Asistencia: {self.usuario.username} - {self.fecha}"
    