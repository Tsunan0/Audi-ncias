"""
URL configuration for projeto_agendador project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_agendador.views import inicial, lista, cadastro, update, editar, deletar, salvar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicial, name='inicial'),
    path('lista/', lista, name='lista'),
    path('cadastro/', cadastro, name='cadastro'),
    path('update/', update, name='update'),
    path('deletar/<int:id>/', deletar, name='deletar'),
    path('editar/<int:id>/', editar, name='editar'),
    path('salvar/<int:id>/', salvar, name='salvar'),

]
