from django import forms
from .models import Documento, TipoDocumento, Unidade, Departamento


class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = '__all__'
        exclude = ('usuario','rev','slug','documento')

class TipoDocumentoForm(forms.ModelForm):
    class Meta:
        model = TipoDocumento
        fields = '__all__'

class UnidadeForm(forms.ModelForm):
    class Meta:
        model = Unidade
        fields = '__all__'

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'