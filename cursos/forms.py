from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model  = Curso
        fields = ['ofertante', 'area', 'certificado', 'tipo', 'link']
        widgets = {
            'ofertante':   forms.Textarea(attrs={'rows': 2}),
            'area':        forms.Textarea(attrs={'rows': 2}),
            'link':        forms.Textarea(attrs={'rows': 2}),
            'certificado': forms.RadioSelect(),
            'tipo':        forms.RadioSelect(),
        }
        labels = {
            'ofertante':  '1. Quem está disponibilizando o curso?',
            'area':       '2. Para qual área é o curso?',
            'certificado':'3. O curso oferece certificado?',
            'tipo':       '4. O curso é pago ou gratuito?',
            'link':       '5. Link de acesso ao curso',
        }