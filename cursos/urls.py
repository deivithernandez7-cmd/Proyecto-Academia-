from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    # ==============================================================================
    # RUTAS DE AUTENTICACIÓN (Login y Cerrar Sesión)
    # ==============================================================================
    path('login/', views.MiLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    # ==============================================================================
    # Rutas basadas en clases (CBV) para Cursos
    # ==============================================================================
    path('web/cursos/', views.CursoListView.as_view(), name='web_lista_cursos'),
    path('web/cursos/<int:pk>/', views.CursoDetailView.as_view(), name='web_detalle_curso'),
    path('web/cursos/nuevo/', views.CursoCreateView.as_view(), name='web_crear_curso'),
    path('web/cursos/<int:pk>/editar/', views.CursoUpdateView.as_view(), name='web_editar_curso'),
    path('web/cursos/<int:pk>/eliminar/', views.CursoDeleteView.as_view(), name='web_eliminar_curso'),

    # ==============================================================================
    # Rutas basadas en clases (CBV) para Profesores (Reto)
    # ==============================================================================
    path('web/profesores/', views.ProfesorListView.as_view(), name='web_lista_profesores'),
    path('web/profesor/<int:pk>/', views.ProfesorDetailView.as_view(), name='web_detalle_profesor'),

    # ==============================================================================
    # Rutas basadas en clases (CBV) para Estudiantes (Paso 3)
    # ==============================================================================
    path('web/estudiantes/', views.EstudianteListView.as_view(), name='web_lista_estudiantes'),
    path('web/estudiantes/<int:pk>/', views.EstudianteDetailView.as_view(), name='web_detalle_estudiante'),
    path('web/estudiantes/nuevo/', views.EstudianteCreateView.as_view(), name='web_crear_estudiante'),
    path('web/estudiantes/<int:pk>/editar/', views.EstudianteUpdateView.as_view(), name='web_editar_estudiante'),
    path('web/estudiantes/<int:pk>/eliminar/', views.EstudianteDeleteView.as_view(), name='web_eliminar_estudiante'),
]
