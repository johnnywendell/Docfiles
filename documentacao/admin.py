from django.contrib import admin
from .models import Documento, TipoDocumento, Unidade, Departamento, Arquivo


class ArquivoInline(admin.TabularInline):
    model = Arquivo
    extra = 0

@admin.register(TipoDocumento)
class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
    )
@admin.register(Unidade)
class UnidadeAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
    )
@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
    )
    
@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    inlines = (ArquivoInline,)
    list_display = (
        '__str__',
        'unidade',
        'documento',
        'departamento',
        'tipodocumento',
    )
