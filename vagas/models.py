from django.db import models

class JobPost(models.Model):
    # Campos existentes
    titulo = models.CharField(default='', max_length=255)
    descricao = models.CharField(max_length=200, default='',)
    cidade = models.CharField(default='São Paulo', max_length=255)
    salario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tipo_contrato = models.CharField(default='CLT', max_length=100, choices=[
        ('CLT', 'CLT'),
        ('PJ', 'PJ'),
        ('Estágio', 'Estágio'),
        ('Freelancer', 'Freelancer'),
    ])
    requisitos = models.CharField(max_length=200, default='',null=True, blank=True)
    beneficios = models.CharField(max_length=200, default='',null=True, blank=True)
    carga_horaria = models.CharField(default='',max_length=50, null=True, blank=True)
    local_trabalho = models.CharField(default='Remoto', max_length=100, choices=[
        ('Presencial', 'Presencial'),
        ('Híbrido', 'Híbrido'),
        ('Remoto', 'Remoto'),
    ], null=True, blank=True)
    
    area_desenvolvimento = models.CharField(default='',max_length=50, choices=[
        ('Backend', 'Backend'),
        ('Frontend', 'Frontend'),
        ('Full Stack', 'Full Stack'),
    ], null=True, blank=True)  # Tipo da vaga
    linguagens_programacao = models.ManyToManyField('LinguagemProgramacao', blank=True  )
    
    link_inscricao = models.URLField(default='',null=True, blank=True)
    idioma_necessario = models.CharField(default='',max_length=255, null=True, blank=True)
    informacoes_empresa = models.CharField(max_length=200, default='',null=True, blank=True)
    data_publicacao = models.DateField(default='2025-01-01', editable=True)
    prazo_inscricao = models.DateField(default='2025-01-01',null=True, blank=True)

    def __str__(self):
        return self.titulo


class LinguagemProgramacao(models.Model):
    nome = models.CharField(
        max_length=50,
        choices=[
            ('Python', 'Python'),
            ('JavaScript', 'JavaScript'),
            ('Java', 'Java'),
            ('C++', 'C++'),
            ('Ruby', 'Ruby'),
            ('PHP', 'PHP'),
            ('C#', 'C#'),
            ('Go', 'Go'),
            ('Swift', 'Swift'),
            ('Kotlin', 'Kotlin'),
        ]
    )


    def __str__(self):
        return self.nome