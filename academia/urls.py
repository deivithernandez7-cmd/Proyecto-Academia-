from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from cursos import views as cursos_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cursos.urls')),

    path('accounts/login/', cursos_views.MiLoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]