from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Curso, Profesor, Estudiante
from .forms import CursoForm, EstudianteForm

# ==============================================================================
# 1. VISTAS PARA CURSOS
# ==============================================================================

class CursoListView(ListView):
    model = Curso
    template_name = 'cursos/lista.html'
    context_object_name = 'cursos'
    paginate_by = 6
    ordering = ['nombre']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_cursos'] = Curso.objects.count()
        context['profesores'] = Profesor.objects.all()
        return context

class CursoDetailView(DetailView):
    model = Curso
    template_name = 'cursos/detalle.html'
    context_object_name = 'curso'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Trae todos los estudiantes registrados para el menú de inscripción
        context['estudiantes_disponibles'] = Estudiante.objects.all()
        return context

class CursoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'cursos/formulario.html'
    success_url = reverse_lazy('web_lista_cursos')
    success_message = "¡El curso '%(nombre)s' fue creado exitosamente!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Nuevo Curso (Protegido)'
        return context

class CursoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'cursos/formulario.html'
    success_url = reverse_lazy('web_lista_cursos')
    success_message = "¡El curso '%(nombre)s' fue actualizado correctamente!"

class CursoDeleteView(LoginRequiredMixin, DeleteView):
    model = Curso
    template_name = 'cursos/curso_confirm_delete.html'
    success_url = reverse_lazy('web_lista_cursos')
    context_object_name = 'curso'

    def delete(self, request, *args, **kwargs):
        curso = self.get_object()
        messages.warning(self.request, f"El curso '{curso.nombre}' fue eliminado del sistema.")
        return super().delete(request, *args, **kwargs)

# ==============================================================================
# 2. VISTAS PARA ESTUDIANTES
# ==============================================================================
class EstudianteListView(ListView):
    model = Estudiante
    template_name = 'cursos/estudiantes_lista.html'  # <-- Asegúrate de que tenga la 's'
    context_object_name = 'estudiantes'
    paginate_by = 5

class EstudianteDetailView(DetailView):
    model = Estudiante
    template_name = 'cursos/estudiante_detalle.html'
    context_object_name = 'estudiante'

class EstudianteCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'cursos/estudiante_formulario.html'
    success_url = reverse_lazy('web_lista_estudiantes')
    success_message = "¡El estudiante '%(nombre)s %(apellido)s' fue registrado con éxito!"

class EstudianteUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'cursos/estudiante_formulario.html'
    success_url = reverse_lazy('web_lista_estudiantes')
    success_message = "¡Los datos del estudiante '%(nombre)s' fueron actualizados correctamente!"

class EstudianteDeleteView(LoginRequiredMixin, DeleteView):
    model = Estudiante
    template_name = 'cursos/estudiante_confirm_delete.html'
    success_url = reverse_lazy('web_lista_estudiantes')
    context_object_name = 'estudiante'

    def delete(self, request, *args, **kwargs):
        estudiante = self.get_object()
        messages.warning(self.request, f"El estudiante '{estudiante.nombre} {estudiante.apellido}' fue eliminado.")
        return super().delete(request, *args, **kwargs)

# ==============================================================================
# 3. VISTAS PARA PROFESORES Y AUTENTICACIÓN
# ==============================================================================

class ProfesorListView(ListView):
    model = Profesor
    template_name = 'cursos/profesores_lista.html'
    context_object_name = 'profesores'
    paginate_by = 3
    ordering = ['nombre']

class ProfesorDetailView(DetailView):
    model = Profesor
    template_name = 'cursos/profesor_detalle.html'
    context_object_name = 'profesor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cursos'] = self.object.cursos.all()
        return context

class MiLoginView(LoginView):
    template_name = 'cursos/registration.html'

    def form_valid(self, form):
        usuario = form.get_user()
        messages.info(self.request, f'¡Bienvenido de nuevo, {usuario.username}!')
        return super().form_valid(form)

# ==============================================================================
# FUNCIÓN DE INSCRIPCIÓN DIRECTA
# ==============================================================================

@login_required
def inscribir_estudiante_curso(request, curso_id):
    if request.method == 'POST':
        estudiante_id = request.POST.get('estudiante_id')
        if estudiante_id:
            curso = get_object_or_404(Curso, pk=curso_id)
            estudiante = get_object_or_404(Estudiante, pk=estudiante_id)
            curso.estudiantes.add(estudiante)
            messages.success(request, f"¡{estudiante.nombre} fue inscrito en {curso.nombre} con éxito!")
    return redirect('web_detalle_curso', pk=curso_id)
