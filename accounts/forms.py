from django.contrib.auth.models import User
from django.contrib.auth import forms


class CustomUserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = forms.UserCreationForm.Meta.fields + ('email','first_name','last_name',)
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
            field.widget.attrs['class'] = 'form-control'

        # Adiciona classe CSS a todos os campos
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        # Personalizar os textos dos campos
        self.fields['username'].label = 'Usuário'
        self.fields['username'].help_text = 'Digite seu nome de usuário. Use apenas letras, números e @/./+/-/_.'

        self.fields['email'].label = 'Endereço de E-mail'
        self.fields['email'].help_text = 'Informe um e-mail válido.'

        self.fields['first_name'].label = 'Primeiro Nome'
        self.fields['first_name'].help_text = ''

        self.fields['last_name'].label = 'Último Nome'
        self.fields['last_name'].help_text = ''

        self.fields['password1'].label = 'Senha'
       