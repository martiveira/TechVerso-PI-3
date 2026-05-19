from django.shortcuts import render, redirect
from django.contrib import messages
from .models import JobPost
from .services import buscar_vagas_externas

def index(request):
    return render(request, 'indexvagas.html')

def list_job_posts(request):
    query  = request.GET.get('q', '').strip()
    source = request.GET.get('source', '')
    local  = request.GET.get('local', '')
    tipo   = request.GET.get('tipo', '')
    novas  = 0

    vagas = JobPost.objects.all().order_by('-data_publicacao', '-id')

    if query:
        novas = buscar_vagas_externas(termo=query)
        vagas = vagas.filter(titulo__icontains=query) | \
                vagas.filter(empresa__icontains=query) | \
                vagas.filter(descricao__icontains=query)

    if source:
        vagas = vagas.filter(source=source)
    if local:
        vagas = vagas.filter(local_trabalho=local)
    if tipo:
        vagas = vagas.filter(tipo_contrato=tipo)

    return render(request, 'vagas/list_job_posts.html', {
        'vagas':            vagas.distinct(),
        'query':            query,
        'source':           source,
        'local':            local,
        'tipo':             tipo,
        'novas_importadas': novas,
    })

def create_job_post(request):
    # sua view existente
    pass