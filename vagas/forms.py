from django import forms
from .models import JobPost, LinguagemProgramacao

class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = ['titulo', 'descricao', 'cidade', 'salario', 'tipo_contrato','requisitos', 'beneficios', 'carga_horaria', 'local_trabalho', 'area_desenvolvimento','linguagens_programacao','link_inscricao','idioma_necessario','informacoes_empresa','data_publicacao','prazo_inscricao']





# from django import forms
# from .models import JobPost

# class JobPostForm(forms.Form):
#     nome = forms.CharField(max_length=100, label='Nome da Vaga')
#     descricao = forms.CharField(widget=forms.Textarea, label='Descrição da Vaga')
#     localizacao = forms.CharField(max_length=100, label='Localização')
#     salario = forms.DecimalField(max_digits=10, decimal_places=2, label='Salário')
#     tipo_contrato = forms.ChoiceField(choices=[
#         ('CLT', 'CLT'),
#         ('PJ', 'PJ'),
#         ('Estágio', 'Estágio'),
#         ('Freelancer', 'Freelancer'),
#     ], label='Tipo de Contrato')
#     data_publicacao = forms.DateField(widget=forms.SelectDateWidget(), label='Data de Publicação')
#     class Meta:
#         model = JobPost  # Associa o formulário ao modelo JobPost
#         fields = ['title', 'description', 'location']  # Campos que serão exibidos no formulário