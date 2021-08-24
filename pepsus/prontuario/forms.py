from django import forms

from prontuario.models import Paciente, Consulta, Medico

class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = ('nome','codigo_sus','data_cadastro', 'ultima_consulta', 'peso', 'altura',
        'data_nascimento', 'sexo', 'cep', 'cidade', 'uf', 'bairro', 'rua', 'numero', 'telefone',
         'email', 'imagem','medico', 'consulta', 'exame', 'sintomas', 'medicacao',  'diagnostico', 
         'observacoes')

        widgets = {
            'nome': forms.TextInput(attrs={ 'class': 'form-control', 
                                            'placeholder':'Maria Joana Fernandes'}),
            'codigo_sus': forms.TextInput(attrs={ 'class': 'form-control', 
                                            'placeholder':'154355455'}),
            'data_cadastro': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),               
            'ultima_consulta': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'peso': forms.TextInput(attrs={ 'class': 'form-control', 
                                            'placeholder':'65,52'}),
            'altura': forms.TextInput(attrs={ 'class': 'form-control', 
                                            'placeholder':'1,65'}),
            'data_nascimento': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'sexo': forms.TextInput(attrs={ 'class': 'form-control', 
                                            'placeholder':'Feminino'}),
            'cep': forms.TextInput(attrs={ 'class': 'form-control', 
                                            'placeholder':'64980-000'}),
            'cidade': forms.TextInput(attrs={ 'class': 'form-control', 
                                            'placeholder':'Corrente'}),
            'uf': forms.TextInput(attrs={ 'class': 'form-control', 
                                            'placeholder':'PI'}),
            'bairro': forms.TextInput(attrs={ 'class': 'form-control', 
                                            'placeholder':'Nova Corrente'}),
            'rua': forms.TextInput(attrs={ 'class': 'form-control', 
                                            'placeholder':'Avelino Ribeiro'}),
            'numero': forms.TextInput(attrs={ 'class': 'form-control', 
                                            'placeholder':'1080'}),
            'telefone': forms.TextInput(attrs={ 'class': 'form-control', 
                                            'placeholder':'89 994224533'}),
            'email': forms.TextInput(attrs={ 'class': 'form-control', 
                                            'placeholder':'E-mail/Não possui'}),
            'imagem': forms.FileInput(attrs={ 'class': 'form-control'}),                              
            'medico': forms.SelectMultiple(attrs={ 'class': 'form-control'}),
            'consulta': forms.Select(attrs={ 'class': 'form-control'}),
            'exame': forms.SelectMultiple(attrs={ 'class': 'form-control'}),
            'sintomas': forms.TextInput(attrs={ 'class': 'form-control',
                                            'placeholder':'Febre'}),
            'medicacao': forms.TextInput(attrs={ 'class': 'form-control', 
                                            'placeholder':'Paracetamol'}),
            'diagnostico': forms.TextInput(attrs={ 'class': 'form-control', 
                                            'placeholder':'...'}),
            'observacoes': forms.TextInput(attrs={ 'class': 'form-control', 
                                            'placeholder':'...'}),
                                            
        }
class ConsultaForm(forms.ModelForm):

    class Meta:
        model = Consulta
        fields = ('tipo','descricao')

        widgets = {
            'tipo': forms.Select(attrs={ 'class': 'form-control', 
                                            'placeholder':'Grave'}),
            'descricao': forms.TextInput(attrs={ 'class': 'form-control', 
                                            'placeholder':'Tempo de espera do paciente'}),
            
        }
class MedicoForm(forms.ModelForm):

    class Meta:
        model = Medico
        fields = ('nome','especialidade','crm')

        widgets = {
            'nome': forms.TextInput(attrs={ 'class': 'form-control', 
                                            'placeholder':'Joaquim Mendes'}),
            'especialidade': forms.TextInput(attrs={ 'class': 'form-control', 
                                            'placeholder':'Clínica Geral'}),
            'crm': forms.TextInput(attrs={ 'class': 'form-control', 
                                            'placeholder':'41258874'}),
        }


       