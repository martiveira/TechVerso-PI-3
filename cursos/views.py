from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Curso
from .forms import CursoForm

def lista_cursos(request):
    query  = request.GET.get('q', '')
    tipo   = request.GET.get('tipo', '')
    cert   = request.GET.get('certificado', '')

    cursos = Curso.objects.filter(ativo=True)

    if query:
        cursos = cursos.filter(ofertante__icontains=query) | \
                 cursos.filter(area__icontains=query)

    if tipo:
        cursos = cursos.filter(tipo=tipo)

    if cert:
        cursos = cursos.filter(certificado=cert)

    return render(request, 'cursos/lista_cursos.html', {
        'cursos': cursos,
        'query':  query,
        'tipo':   tipo,
        'cert':   cert,
    })

def form_cursos(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = form.save(commit=False)
            if request.user.is_authenticated:
                curso.criado_por = request.user
            curso.save()
            messages.success(request, 'Curso cadastrado com sucesso!')
            return redirect('cursos:lista')
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = CursoForm()

    return render(request, 'cursos/form_cursos.html', {'form': form})