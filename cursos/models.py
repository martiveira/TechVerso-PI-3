from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    CERTIFICADO_CHOICES = [
        ('Sim', 'Sim'),
        ('Não', 'Não'),
        ('Não sei', 'Não sei'),
    ]
    TIPO_CHOICES = [
        ('Gratuito', 'Gratuito'),
        ('Gratuitos e Pagos', 'Gratuitos e Pagos'),
        ('Pago', 'Pago'),
        ('Não sei', 'Não sei'),
    ]

    ofertante    = models.CharField(max_length=200)
    area         = models.CharField(max_length=200)
    certificado  = models.CharField(max_length=10, choices=CERTIFICADO_CHOICES)
    tipo         = models.CharField(max_length=20, choices=TIPO_CHOICES)
    link         = models.TextField()
    criado_por   = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    data_criacao = models.DateTimeField(auto_now_add=True)
    ativo        = models.BooleanField(default=True)

    class Meta:
        ordering = ['-data_criacao']

    def __str__(self):
        return f"{self.ofertante} — {self.area}"