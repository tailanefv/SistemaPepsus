from django.urls import path
from . import views 

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('sobre', views.sobre, name='sobre'),
    path('listar_pacientes', views.listar_pacientes, name='listar_pacientes'),
    path('listar_exames', views.listar_exames, name='listar_exames'),
    path('listar_consultas', views.listar_consultas, name='listar_consultas'),
    path('listar_medicos', views.listar_medicos, name='listar_medicos'),

    path('paciente/<int:id>/', views.detalhar_paciente, name='detalhar_paciente'), 
    path('paciente/new/', views.cadastrar_paciente, name='cadastrar_paciente'),
    path('paciente/editar/<int:id>/', views.editar_paciente, name='editar_paciente'),
    path('buscar_paciente', views.buscar_paciente, name='buscar_paciente'),

    path('page_login', views.page_login, name='page_login'),
    path('autenticar_usuario', views.autenticar_usuario, name='autenticar_usuario'),
    path('logout_usuario', views.logout_usuario, name='logout_usuario'),

    path('consulta/<int:id>/', views.detalhar_consulta, name='detalhar_consulta'), 
   
    path('medico/<int:id>/', views.detalhar_medico, name='detalhar_medico'),
    path('medico/new/', views.cadastrar_medico, name='cadastrar_medico'),
    path('medico/editar/<int:id>/', views.editar_medico, name='editar_medico'),
    
    path('paciente/deletar/<int:id>/', views.deletar_paciente, name='deletar_paciente'),
    path('medico/deletar/<int:id>/', views.deletar_medico, name='deletar_medico'),
]