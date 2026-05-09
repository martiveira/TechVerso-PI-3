from django.shortcuts import render, redirect
from django.urls import reverse  # Importação corrigida
from django.http import HttpResponse
from .models import JobPost, LinguagemProgramacao
from .forms import JobPostForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'indexvagas.html')
    create_url = reverse('create')  # Gera a URL para 'create'
    list_url = reverse('list')  # Gera a URL para 'list'
    return HttpResponse(f"""
        <p>Aqui falaremos sobre as vagas.</p>
        <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="{create_url}">Postar Vagas</a></li>
            <li><a class="dropdown-item" href="{list_url}">Listar Vagas</a></li>
        </ul>
        <button onclick="window.history.back()">Voltar</button>
    """)

def form_django(request):
    form = JobPostForm()
    context = {
        'form': form,
    }
    return render(request, '/templates/create_job_post.html', context=context)

@login_required
def create_job_post(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            form.save()  # Salva os dados no banco de dados
            return redirect('list')  # Redireciona para a página de listagem
    else:
        form = JobPostForm()
    return render(request, 'create_job_post.html', {'form': form})

def list_job_posts(request):
    jobs = JobPost.objects.all()

    # Filtragem
    titulo = request.GET.get('titulo')
    descricao = request.GET.get('descricao')
    cidade = request.GET.get('cidade')
    salario = request.GET.get('salario')
    tipo_contrato = request.GET.get('tipo_contrato')

    if titulo:
        jobs = jobs.filter(titulo__icontains=titulo)
    if descricao:
        jobs = jobs.filter(descricao__icontains=descricao)
    if cidade:
        jobs = jobs.filter(cidade__icontains=cidade)
    if salario:
        try:
            salario = float(salario)
            jobs = jobs.filter(salario=salario) # Ou salario__gte/lte para faixas
        except ValueError:
            pass # Ignora se o valor do salário não for um número válido
    if tipo_contrato:
        jobs = jobs.filter(tipo_contrato=tipo_contrato)

    # Ordenação
    ordenacao = request.GET.get('ordenacao')
    if ordenacao:
        jobs = jobs.order_by(ordenacao)

    context = {'jobs': jobs}
    return render(request, 'list_job_posts.html', context)