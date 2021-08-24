from django.shortcuts import render, get_object_or_404, redirect
from prontuario.models import Medico, Exame, Consulta, Paciente
from prontuario.forms import PacienteForm, ConsultaForm,  MedicoForm
from django.contrib.auth import authenticate, login, logout

def deletar_medico(request, id):
    medico = get_object_or_404(Medico, pk=id)
    if request.method=='POST':
        medico.delete()
        return redirect(listar_medicos)
    else:
        return render(request, 'prontuario/apagar_medico.html', {'medico':medico})

def deletar_paciente(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    if request.method=='POST':
        paciente.delete()
        return redirect(listar_pacientes)
    else:
        return render(request, 'prontuario/apagar_paciente.html', {'paciente':paciente})

	

def editar_medico(request, id):
    medico = get_object_or_404(Medico, pk=id)
    if request.method == "POST":
        form = MedicoForm(request.POST, request.FILES, instance=medico)
        if form.is_valid():
            medico = form.save(commit=False)
            form.save()
            return redirect('detalhar_medico', id=medico.id)
    else:
        form = MedicoForm(instance=medico)
    return render(request, 'prontuario/editar_medico.html', {'form': form})


def cadastrar_medico(request):
    if request.method == "POST":
        form = MedicoForm(request.POST, request.FILES)
        if form.is_valid():
            medico = form.save(commit=False)
            form.save()
            return redirect('detalhar_medico', id=medico.id)
    else:
        form = MedicoForm()
    return render(request, 'prontuario/editar_medico.html', {'form': form})


def detalhar_medico(request, id):
    medico = get_object_or_404(Medico, pk=id)
    return render(request, 'prontuario/detalhar_medico.html', {'medico':medico})


def detalhar_consulta(request, id):
    consulta = get_object_or_404(Consulta, pk=id)
    return render(request, 'prontuario/detalhar_consulta.html', {'consulta':consulta})

def logout_usuario(request):
    logout(request)
    return render(request, 'prontuario/login.html',{})

def autenticar_usuario(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        pacientes = Paciente.objects.all()
        return render(request, 'prontuario/listar_pacientes.html', {'pacientes':pacientes})
    else:
        return render(request, 'prontuario/login.html',{})

def page_login(request):
    return render(request, 'prontuario/login.html',{})

def buscar_paciente(request):
    infor = request.POST['infor']
    pacientes = Paciente.objects.filter(nome__contains=infor)
    return render(request, 'prontuario/listar_pacientes.html', {'pacientes':pacientes})

def editar_paciente(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    if request.method == "POST":
        form = PacienteForm(request.POST, request.FILES, instance=paciente)
        if form.is_valid():
            paciente = form.save(commit=False)
            form.save()
            return redirect('detalhar_paciente', id=paciente.id)
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'prontuario/editar_paciente.html', {'form': form})


def cadastrar_paciente(request):
    if request.method == "POST":
        form = PacienteForm(request.POST, request.FILES)
        if form.is_valid():
            paciente = form.save(commit=False)
            form.save()
            return redirect('detalhar_paciente', id=paciente.id)
    else:
        form = PacienteForm()
    return render(request, 'prontuario/editar_paciente.html', {'form': form})

def detalhar_paciente(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    return render(request, 'prontuario/detalhar_paciente.html', {'paciente':paciente})


def listar_consultas(request):
    consultas = Consulta.objects.all()
    return render(request, 'prontuario/listar_consultas.html', {'consultas':consultas})

def listar_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'prontuario/listar_medicos.html', {'medicos':medicos})

def listar_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'prontuario/listar_pacientes.html', {'pacientes':pacientes})

def listar_exames(request):
    pacientes = Paciente.objects.all()
    return render(request, 'prontuario/listar_pacientes.html', {'pacientes':pacientes})

def pagina_inicial(request):
    return render(request, 'prontuario/pagina_inicial.html', {})


def sobre(request):
    return render(request, 'prontuario/sobre.html', {})