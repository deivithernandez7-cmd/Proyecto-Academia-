from django import forms
from .models import Estudiante, Curso

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'email', 'matricula']
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'codigo', 'profesor', 'estudiantes']
        
        labels = {
            'nombre': 'Nombre del Curso',
            'codigo': 'Código Único',
            'profesor': 'Profesor Asignado (ForeignKey)',
            'estudiantes': 'Estudiantes Inscritos (ManyToManyField)',
        }
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Programación Python'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. PY101'}),
            'profesor': forms.Select(attrs={'class': 'form-select'}),
            'estudiantes': forms.SelectMultiple(attrs={'class': 'form-select', 'size': '5'}),
        }

    # Esta función va alineada con 'class Meta' (4 espacios de sangría)
    def clean_codigo(self):
        codigo = self.cleaned_data.get('codigo')
        if len(codigo) < 4:
            raise forms.ValidationError("El código debe tener al menos 4 caracteres.")
        return codigo.upper()
