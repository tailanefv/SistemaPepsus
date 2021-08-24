from django.db import models
from django.conf import settings


class Medico(models.Model):
    nome = models.CharField(max_length=200)
    especialidade = models.CharField(max_length=40)
    crm = models.CharField(max_length=8)

    def __str__(self):
        return self.nome 

class Exame(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome 

class Consulta(models.Model):
    tipo = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self):
        return self.tipo
    

class Paciente(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)
    codigo_sus = models.CharField(max_length=20)
    data_cadastro = models.DateField(null=False, blank=False)
    ultima_consulta = models.DateField(null=False, blank=False)

    peso = models.CharField(max_length=5)
    altura = models.CharField(max_length=5)
    data_nascimento = models.DateField(null=False, blank=False)
    sexo = models.CharField(max_length=9)

    cep = models.CharField(max_length=10)
    cidade = models.CharField(max_length=20)
    uf = models.CharField(max_length=20)
    bairro = models.CharField(max_length=30)
    rua = models.CharField(max_length=30)
    numero = models.CharField(max_length=20)

    telefone = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='prontuario/media', blank=True)

    medico = models.ManyToManyField(Medico, blank = True)
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE, verbose_name="Consulta")
    exame = models.ManyToManyField(Exame, blank = True)
    sintomas = models.CharField(max_length=30)
    medicacao = models.CharField(max_length=40)
    diagnostico = models.CharField(max_length=100)
    observacoes = models.TextField()
        
    def __str__(self):
        return self.nome 
